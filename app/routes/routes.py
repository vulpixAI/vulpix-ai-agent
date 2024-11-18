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
        "https://lh3.googleusercontent.com/pw/AIL4fc-cY2NZaUkY03qTxDZ6BuUJmuhFd_dxaF1k3Tm5t1S_JmGhTQ-gKbKXGDUZadtxRnbz5XLTiGnG3iOYbgHVizGP5hQDHMb9oPM86_VrHlEJKmld7iT9l3mDey2fFGPAoBPhiLouS-SuPN9KkyhoDxmQ=w1138-h1135-s-no?authuser=0",
        "https://leonardo-cdn.b-cdn.net/wp-content/uploads/2023/07/0-2022-12-02T033131-1.png",
        "https://www.promptpal.net/_next/image?url=https%3A%2F%2Fcdn.sanity.io%2Fimages%2Fe3itcv4k%2Fproduction%2F7ce0ff9d56ddc96e39982b6025f1e5779a7ff0e8-1536x2304.jpg&w=750&q=75",
        "https://miro.medium.com/v2/resize:fit:1024/1*5Xc1yC5c__spfn_halRugw.jpeg"
    ]
    return {
        "image_urls": image_urls,
        "caption": "Teste mockado"
    }