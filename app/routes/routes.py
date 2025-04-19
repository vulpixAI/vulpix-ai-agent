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
        "https://sdmntpritalynorth.oaiusercontent.com/files/00000000-94a0-6246-b7dd-b3b51fc92194/raw?se=2025-04-19T20%3A47%3A19Z&sp=r&sv=2024-08-04&sr=b&scid=3c7a8a9e-9233-5528-9a15-cd10036e725e&skoid=a3336399-497e-45e5-8f28-4b88ecca3d1f&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2025-04-19T18%3A28%3A05Z&ske=2025-04-20T18%3A28%3A05Z&sks=b&skv=2024-08-04&sig=7wK1bEUrz1U9t5ltCtYWwJw99MT5rcd24Q/ZqfHz31U%3D",
        "https://avatars.githubusercontent.com/u/142420909?v=4",
        "https://sdmntpreastus2.oaiusercontent.com/files/00000000-51f4-51f6-8fbb-9af6abd712c2/raw?se=2025-04-19T21%3A12%3A40Z&sp=r&sv=2024-08-04&sr=b&scid=5a095d6f-40e6-5f33-bf0f-372f87c12bc8&skoid=a3336399-497e-45e5-8f28-4b88ecca3d1f&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2025-04-19T18%3A27%3A02Z&ske=2025-04-20T18%3A27%3A02Z&sks=b&skv=2024-08-04&sig=XKM/gZD9eJmP6p/ntn1rh9vqpGib062TfkwJyFuLLsI%3D"
    ]
    return {
        "image_urls": image_urls,
        "caption": "Teste mockado"
    }