# routes.py
from flask import Flask, request, jsonify
from app.generate_content import generate_content
from services.gemini_service import generate_prompt

app = Flask(__name__)

#geração de prompt
@app.route('/generate-prompt', methods=['POST'])
def create_prompt():
    data = request.json
    form_data = data.get('form_data')
    prompt = generate_prompt(form_data)
    return jsonify({"prompt": prompt})

#geração de imagem e legenda
@app.route('/generate-content', methods=['POST'])
def create_content():
    data = request.json
    prompt = data.get('prompt')
    user_request = data.get('user_request')
    
    result = generate_content(prompt, user_request)
    
    return jsonify(result)
