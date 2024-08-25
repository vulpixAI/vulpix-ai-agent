import google.generativeai as genai
import json

# Configuração da API
GOOGLE_API_KEY = ''
genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel("gemini-1.5-flash")

# Carregar o JSON 
with open('C:/Users/Renan Casalle/Desktop/vulpix-ai-agent/app/formulario.json', 'r', encoding='utf-8') as f:
    form_data = json.load(f)

form_str = json.dumps(form_data, indent=2)

prompt = form_str + "Please generate a creative and detailed image description for stable diffusion."

response = model.generate_content(prompt)

print(response)