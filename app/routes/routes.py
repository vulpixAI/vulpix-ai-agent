from flask import Flask, request, jsonify
from flask_swagger_ui import get_swaggerui_blueprint
from app.routes.generate_content import generate_content
from services.gemini_service import generate_prompt
from services.gemini_service import generate_caption
from app.utils.config import AMBIENTE

app = Flask(__name__)

SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'
swagguerui_blueprint = get_swaggerui_blueprint(SWAGGER_URL, API_URL)
app.register_blueprint(swagguerui_blueprint, url_prefix=SWAGGER_URL)

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
        if AMBIENTE == 'DEV':
            return mock_json()
        else:
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

def mock_json():
    image_urls = [
        "https://cdn.leonardo.ai/users/4f747aa7-238a-4900-bad3-93a7e2a41968/generations/5e617e68-a632-4607-9604-7d1825666f5f/Leonardo_Phoenix_A_vibrant_and_playful_image_capturing_the_joy_1.jpg?w=512",
        "https://cdn.leonardo.ai/users/4f747aa7-238a-4900-bad3-93a7e2a41968/generations/d99af10c-c366-4963-82af-741bdd4ddf9f/Leonardo_Phoenix_Unlocking_Happy_FeetOverall_ConceptA_vibrant_3.jpg?w=512",
        "https://cdn.leonardo.ai/users/4f747aa7-238a-4900-bad3-93a7e2a41968/generations/d99af10c-c366-4963-82af-741bdd4ddf9f/Leonardo_Phoenix_Unlocking_Happy_FeetOverall_ConceptA_vibrant_0.jpg?w=512",
        "https://cdn.leonardo.ai/users/4f747aa7-238a-4900-bad3-93a7e2a41968/generations/5e617e68-a632-4607-9604-7d1825666f5f/Leonardo_Phoenix_A_vibrant_and_playful_image_capturing_the_joy_2.jpg?w=512"
    ]
    return {
        "image_urls": image_urls,
        "caption": "Teste mockado"
    }