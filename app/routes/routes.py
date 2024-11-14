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
            # data = request.json
            # prompt = data.get('prompt')
            # user_request = data.get('user_request')
            
            # result = generate_content(prompt, user_request)
            # return jsonify(result)
            return null
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
        "https://scontent.cdninstagram.com/v/t51.2885-15/465612471_1832441967561171_5765861591217010485_n.jpg?_nc_cat=104&ccb=1-7&_nc_sid=18de74&_nc_ohc=0UotgaD99foQ7kNvgH834VS&_nc_zt=23&_nc_ht=scontent.cdninstagram.com&edm=AM6HXa8EAAAA&oh=00_AYAiwgFpHGZ5x8S0XHoTd7UZ8YgkzgAaHS1HWf9ZCRnr7w&oe=673A994B",
        "https://scontent.cdninstagram.com/v/t51.2885-15/465603063_1594588258145224_3558823223195028993_n.jpg?_nc_cat=101&ccb=1-7&_nc_sid=18de74&_nc_ohc=4t9cavUlJ1AQ7kNvgGHL0O-&_nc_zt=23&_nc_ht=scontent.cdninstagram.com&edm=AM6HXa8EAAAA&oh=00_AYCErLRIly4QuFq50bL0mFpDz0U7c7i3V1frLUNdDQO2ng&oe=673A864F",
        "https://scontent.cdninstagram.com/v/t51.2885-15/465437823_8755403637861308_4625396683262565077_n.jpg?_nc_cat=100&ccb=1-7&_nc_sid=18de74&_nc_ohc=47jyD0pjsw0Q7kNvgF1o1HM&_nc_zt=23&_nc_ht=scontent.cdninstagram.com&edm=AM6HXa8EAAAA&oh=00_AYAIb5Qjo8YVHhiXxV14m4iwECd8yIxKK8qbWUF-PdHIww&oe=673A94FD",
        "https://scontent.cdninstagram.com/v/t51.2885-15/465579744_3765236240472987_173456101577689593_n.jpg?_nc_cat=110&ccb=1-7&_nc_sid=18de74&_nc_ohc=74AJnCw_mrEQ7kNvgHxkwn8&_nc_zt=23&_nc_ht=scontent.cdninstagram.com&edm=AM6HXa8EAAAA&oh=00_AYCWCIrjorBjDdA1SDKg0JFqCgq3HLfziD3xaQ2fgy9dVg&oe=673A7CEF"
    ]
    return {
        "image_urls": image_urls,
        "caption": "Teste mockado"
    }