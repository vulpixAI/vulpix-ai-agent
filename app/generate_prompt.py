import google.generativeai as genai
import json 
import psycopg2
import os 
from dotenv import load_dotenv

load_dotenv()

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

cursor.execute("SELECT informacao FROM informacoes WHERE id = 4;")

info_user = cursor.fetchone()

def prompt_generator(info_user):
    form_dict = info_user[0]  

    form_str = json.dumps(form_dict, indent=4)

    prompt = form_str + """
    I will provide you with detailed information about a company, including its name, sector, branding, and target audience. Your task is to generate a high-quality English prompt for Stable Diffusion, which will 
    create a visual representation based on the company's values, products, and aesthetic preferences. The generated prompt should include the following key elements:
    Overall Concept: A brief description of the visual goal for the image, incorporating the company's unique selling proposition (USP) and branding.
    Background: A detailed description of the background design, colors, and visual style that align with the company's identity.
    Foreground Elements: Focus on the main products or services of the company, emphasizing their features and appeal. 
    Describe the positioning of these elements to create a balanced and visually engaging image.
    Text Elements: Include any important marketing or promotional text that should be part of the image (for example, a call to action or slogan). 
    Provide guidelines on font style and placement.
    Color Palette: Define the primary, secondary, and accent colors used in the image, based on the company's brand guidelines.
    Audience and Tone: Define the target audience and the overall tone or mood of the image.
    Final Goal: Specify the intended emotional impact or action you want the viewer to take after seeing the image (for example, urgency to purchase or visit a website).
    """

    response = model.generate_content(prompt)

    prompt_final = response.text

    print(prompt_final)

    cursor.execute("UPDATE informacoes SET user_prompt = %s WHERE id = 4;", (prompt_final,))

    connection.commit()
  

if info_user:
    generate_prompt(info_user)