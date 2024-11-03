# gemini_service.py
import google.generativeai as genai
from app.utils.config import GOOGLE_API_KEY

genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel(model_name="gemini-1.5-flash")

def generate_prompt(form_data):
    # Define o texto da solicitação para a API de geração de conteúdo
    request_text = f"""
    Transform the following form data into a detailed, English-language prompt for an image generation model. 
    Ensure that all information provided in the form is incorporated into the prompt. The prompt should be structured to 
    guide the image generation model (e.g., Stable Diffusion) to create a visually accurate and contextually relevant image.

    Form data:
    {form_data}

    The generated prompt should be in English.
    """
    response = model.generate_content(request_text)

    generated_text = getattr(response, 'text', "Prompt generation failed.")  
    return {"prompt": generated_text}

def generate_caption(description):
    request_caption = f"""
    Based on the following description, generate a concise and engaging caption suitable for social media. 
    Ensure the caption is in English and highlights the key elements effectively.

    Description:
    {description}
    """
    response = model.generate_content(request_caption)
    return response.text

def generate_request(prompt, user_request):
    request_text = f"""
        Combine the following information into a single, detailed prompt for Stable Diffusion, limited to a maximum of 1100 characters. 
        The prompt should create an eye-catching image that reflects the user’s request while incorporating the company’s branding and values.
        
        Base Prompt:
        {prompt}

        User Request:
        {user_request}

        Please generate a cohesive and concise prompt in English that naturally integrates the main elements of both inputs, staying within the character limit.
    """
    response = model.generate_content(request_text)
    return response

