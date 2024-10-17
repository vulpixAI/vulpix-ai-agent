import google.generativeai as genai
import psycopg2
import json
import os
import requests
from dotenv import load_dotenv

load_dotenv()

# Configuração do Google Gemini API
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")

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
    A imagem deve ter um fundo de natureza com vegetação verde e luz natural, destacando um ventilador solar em uso. O logotipo da EcoBreeze e o slogan 'Ventilando o 
    Futuro Sustentável' devem estar presentes, com um estilo clean e moderno, transmitindo a ideia de simplicidade, inovação e compromisso com a sustentabilidade.
    """

    request_image = user_request_image + form_str + """
    Generate a single, detailed prompt for Stable Diffusion that creates an eye-catching image. The image should reflect the user’s request and incorporate their company’s branding and values. max 1500 characters.
    """

    response = model.generate_content(request_image)
    return response.text

def generate_image(prompt_text):
    url = "https://cloud.leonardo.ai/api/rest/v1/generations"
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "authorization": "Bearer 75839dd1-02b8-45c0-b33d-96e44c7c44ff"
    }
    
    payload = {
        "alchemy": True,
        "height": 768,
        "modelId": "b24e16ff-06e3-43eb-8d33-4416c2d75876",
        "num_images": 4,
        "presetStyle": "DYNAMIC",
        "prompt": prompt_text,
        "width": 1024
    }
    
    response = requests.post(url, json=payload, headers=headers)
    return response.json()

def main():
    prompt_text = generate_prompt()
    image_data = generate_image(prompt_text)
    print("Dados da imagem gerada:", image_data)

if __name__ == "__main__":
    main()
