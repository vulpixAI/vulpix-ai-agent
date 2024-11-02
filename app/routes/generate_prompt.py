# generate_prompt.py
from services.gemini_service import generate_prompt

def create_prompt_from_form(form_data):
    prompt = generate_prompt(form_data)
    return prompt
