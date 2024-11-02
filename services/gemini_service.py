import google.generativeai as genai
from app.utils.config import GOOGLE_API_KEY

genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")

def generate_prompt(form_data):
    request_text = form_data + """
    Generate a single, detailed prompt for Stable Diffusion that creates an eye-catching image. 
    The image should reflect the user’s request and incorporate their company’s branding and values. max 1300 characters.
    """
    response = model.generate_content(request_text)
    return response.text

def generate_caption(description):
    request_caption = description + """
    Transform the following pieces of information into a single, concise block of text suitable for a short social media caption. 
    Ensure the content is engaging, clear, and highlights key details. Return the caption in Portuguese.
    """
    response = model.generate_content(request_caption)
    return response.text
