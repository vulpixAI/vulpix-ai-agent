from flask import Flask, request, jsonify
from services.gemini_service import generate_prompt, generate_caption
from services.leonardo_service import generate_image, poll_for_image_links

app = Flask(__name__)

@app.route('/generate-prompt', methods=['POST'])
def create_prompt():
    data = request.json
    form_data = data.get('form_data')
    prompt = generate_prompt(form_data)
    return jsonify({"prompt": prompt})

@app.route('/generate-content', methods=['POST'])
def create_content():
    data = request.json
    prompt = data.get('prompt')
    user_request = data.get('user_request')
    
    #cria a imagem
    image_data = generate_image(prompt)
    generation_id = image_data.get("sdGenerationJob", {}).get("generationId")
    if not generation_id:
        return jsonify({"error": "Failed to obtain generation ID"}), 500
    
    #obtem links das imagens geradas
    image_urls = poll_for_image_links(generation_id)
    
    caption = generate_caption(user_request)
    
    return jsonify({
        "image_urls": image_urls,
        "caption": caption
    })
