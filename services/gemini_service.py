import google.generativeai as genai
from app.utils.config import GOOGLE_API_KEY

genai.configure(api_key=GOOGLE_API_KEY)

#model = genai.GenerativeModel(model_name="gemini-1.5-flash")
model = genai.GenerativeModel('gemini-pro')

def generate_prompt(form_data):
    request_text = f"""
    Transform the following form data into a clear, detailed prompt for an image generation model. Incorporate all information from 
    the form thoroughly into the prompt. The resulting prompt should be structured to guide the image generation model (such as Stable Diffusion) 
    to produce an image that is both visually accurate and contextually relevant. Ensure the prompt is concise and strictly limited to a maximum of 1300 characters.
    Form data:
    {form_data}

    The generated prompt should be in English.
    """
    response = model.generate_content(request_text)

    generated_text = getattr(response, 'text', "Prompt generation failed.")  
    return {"prompt": generated_text}

def generate_caption(prompt, user_request):
    request_caption = f"""
    Based on the following prompt and user request, generate a concise and engaging caption suitable for social media. 
    The caption should be in Brazilian Portuguese and should highlight the key elements effectively.

    Prompt:
    {prompt}

    User Request:
    {user_request}

    Caption in Brazilian Portuguese:
    """
    response = model.generate_content(request_caption)
    return response.text.strip()

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
    return response.text

