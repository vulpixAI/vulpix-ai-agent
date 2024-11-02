import google.generativeai as genai
import psycopg2
import json
import os
import requests
import time  
from dotenv import load_dotenv
from view_image import LeonardoStatusChecker

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")

LEONARDO_API_KEY = os.getenv("LEONARDO_API_KEY")

connection = psycopg2.connect(
    database="vulpix",
    host="localhost",
    user="postgres",
    password="30112004",
    port="5432"
)

cursor = connection.cursor()
cursor.execute("SELECT user_prompt FROM informacoes WHERE id = 2;")
info_user = cursor.fetchone()

def generate_prompt():
    form_dict = info_user[0]
    form_str = json.dumps(form_dict, indent=4)

    user_request_image = """
    A imagem deve retratar um grupo de pessoas em um barco navegando em águas tranquilas, com o céu azul claro ao fundo. 
    Um ventilador solar EcoBreeze está em destaque no convés, refrescando os passageiros enquanto eles relaxam e aproveitam a brisa. 
    O logotipo da EcoBreeze deve estar visível no ventilador, e o slogan 'Ventilando o Futuro Sustentável' deve aparecer de forma discreta, 
    destacando o compromisso com a sustentabilidade. A imagem deve transmitir 
    uma sensação de conforto e alívio do calor durante a navegação, com um toque de inovação e modernidade.
    """

    request_image = user_request_image + form_str + """
    Generate a single, detailed prompt for Stable Diffusion that creates an eye-catching image. The image should reflect the user’s request and incorporate their company’s branding and values. max 1300 characters.
    """

    response = model.generate_content(request_image)
    return response.text

def generate_image(prompt_text):
    url = "https://cloud.leonardo.ai/api/rest/v1/generations"
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "authorization": "Bearer " + LEONARDO_API_KEY
    }
    
    payload = {
        "alchemy": True,
        "height": 768,
        "modelId": "6b645e3a-d64f-4341-a6d8-7a3690fbf042", 
        "num_images": 4,
        "presetStyle": "DYNAMIC",
        "prompt": prompt_text,
        "width": 1024
    }
    
    response = requests.post(url, json=payload, headers=headers)
    
    return response.json()

def poll_for_image_links(id_image, api_key, max_attempts=10, wait_time=5):
    checker = LeonardoStatusChecker(id_image, api_key)
    
    for attempt in range(max_attempts):
        image_urls = checker.get_image_urls()
        
        if image_urls:
            return image_urls
        else:
            print(f"Tentativa {attempt + 1}/{max_attempts}: Aguardando {wait_time} segundos para tentar novamente.")
            time.sleep(wait_time)

    print("Número máximo de tentativas atingido. Não foi possível obter as URLs das imagens.")
    return []

def main():
    prompt_text = generate_prompt()
    image_data = generate_image(prompt_text)
    
    id_image = image_data.get("sdGenerationJob", {}).get("generationId")

    if not id_image:
        print("Erro: Não foi possível obter o generationId.")
        return

    #cursor.execute("UPDATE informacoes SET generation_id = %s WHERE id = 2;", (id_image,))
    #connection.commit()

    image_urls = poll_for_image_links(id_image, LEONARDO_API_KEY, max_attempts=10, wait_time=5)
    
    if image_urls:
        print("URLs das imagens geradas:")
        for url in image_urls:
            print(url)
    else:
        print("Nenhuma URL de imagem encontrada.")

if __name__ == "__main__":
    main()
