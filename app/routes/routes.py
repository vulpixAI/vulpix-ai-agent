from flask import Flask, request, jsonify
from app.routes.generate_content import generate_content
from services.gemini_service import generate_prompt
from services.gemini_service import generate_caption

app = Flask(__name__)

@app.route('/generate-prompt', methods=['POST'])
def create_prompt():
    try:
        data = request.json
        form_data = data.get('form_data')
        if not form_data:
            raise ValueError("form_data não foi fornecido na requisição")
        
        response = generate_prompt(form_data)
        
        return jsonify(response) 
    except Exception as e:
        print(f"Erro no /generate-prompt: {e}")
        return jsonify({"error": f"Erro ao gerar o prompt: {str(e)}"}), 500



@app.route('/generate-content', methods=['POST'])
def create_content():
    try:
        data = request.json
        prompt = data.get('prompt')
        user_request = data.get('user_request')
        
        result = generate_content(prompt, user_request)
        return jsonify(result)
    except Exception as e:
        print(f"Erro no /generate-content: {e}")
        return jsonify({"error": f"Erro ao gerar conteúdo: {str(e)}"}), 500
    
    
@app.route('/generate-caption', methods=['POST'])
def generate_caption_route():
    try:
        data = request.json
        prompt = data.get('prompt')
        user_request = data.get('user_request')
        
        # Verifica se o prompt e user_request foram fornecidos
        if not prompt or not user_request:
            return jsonify({"error": "prompt e/ou user_request não foram fornecidos na requisição"}), 400

        # Gera a legenda usando prompt e user_request
        response = generate_caption(prompt, user_request)
        return response
    except Exception as e:
        print(f"Erro no /generate-caption: {e}")
        return jsonify({"error": f"Erro ao gerar legenda: {str(e)}"}), 500
