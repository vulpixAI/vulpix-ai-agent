# gemini_service.py
import google.generativeai as genai
from app.utils.config import GOOGLE_API_KEY

genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel(model_name="gemini-1.5-flash")

def generate_prompt(form_data):
    request_text = f"""
    Transform the following form data into a detailed, English-language prompt for an image generation model. 
    Ensure that all information provided in the form is incorporated into the prompt. The prompt should be structured to 
    guide the image generation model (e.g., Stable Diffusion) to create a visually accurate and contextually relevant image.

    Form data:
    {form_data}

    The generated prompt should be in English.
    """
    response = model.generate_text(request_text)
    return response.result

def generate_caption(description):
    request_caption = f"""
    Based on the following description, generate a concise and engaging caption suitable for social media. 
    Ensure the caption is in English and highlights the key elements effectively.

    Description:
    {description}
    """
    response = model.generate_text(request_caption)
    return response.result
