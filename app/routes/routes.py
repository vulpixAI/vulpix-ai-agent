from flask import Flask, request, jsonify
from app.routes.generate_content import generate_content
from services.gemini_service import generate_prompt
from services.gemini_service import generate_caption
from app.utils.config import AMBIENTE

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
        "https://avatars.githubusercontent.com/u/83714306?v=4",
        "https://media.licdn.com/dms/image/v2/D4D03AQHWCQmpIUBSzg/profile-displayphoto-shrink_200_200/profile-displayphoto-shrink_200_200/0/1727672217059?e=2147483647&v=beta&t=0bGpO80n_89w-1KyOBNwZjPsnteTDDZGVyHoMguE_k0",
        "https://avatars.githubusercontent.com/u/142420909?v=4",
        "https://media.licdn.com/dms/image/v2/D4D03AQGgU0JTKFdEcQ/profile-displayphoto-shrink_200_200/profile-displayphoto-shrink_200_200/0/1703171602261?e=2147483647&v=beta&t=u4jvPyQXJLWxWkbEXcsEe_l7gzNGh0nbgp1Ohab81n0"
    ]
    return {
        "image_urls": image_urls,
        "caption": "Teste mockado"
    }