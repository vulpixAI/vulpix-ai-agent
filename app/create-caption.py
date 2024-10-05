import google.generativeai as genai
import psycopg2
import json

GOOGLE_API_KEY = ''
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

cursor.execute("SELECT informacao FROM informacoes WHERE id = 4;")
info_user = cursor.fetchone()

def create_request_ai():
    form_dict = info_user[0]  

    form_str = json.dumps(form_dict, indent=4)

    user_request_image = """
    A imagem deve ter um fundo de natureza com vegetação verde e luz natural, destacando um ventilador solar em uso. O logotipo da EcoBreeze e o slogan 'Ventilando o 
    Futuro Sustentável' devem estar presentes, com um estilo clean e moderno, transmitindo a ideia de simplicidade, inovação e compromisso com a sustentabilidade.
    """

    request_caption = user_request_image + form_str + """
    ransform the following pieces of information into a single, concise block of text suitable for a short social media caption. Ensure the content is engaging, clear, and highlights key details. Return the caption in Portuguese.
    """

    response = model.generate_content(request_caption)

    print(response.text)

create_request_ai()

cursor.close()
connection.close()
