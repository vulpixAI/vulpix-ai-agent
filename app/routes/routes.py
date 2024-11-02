from flask import Flask, request, jsonify
from app.routes.generate_image import image_generator
from app.routes.generate_caption import caption_generator
from app.routes.generate_prompt import prompt_generator
from app.view_image import check_status, get_image_urls

app = Flask(__name__)

@app.route('/generate-image', methods=['POST'])
def image_generator():
    data = request.json
    prompt = data.get('prompt')
    model_id = data.get('model_id')
    result = image_generator(prompt, model_id)
    return jsonify(result)

@app.route('/generate-caption', methods=['POST'])
def caption_generator():
    data = request.json
    description = data.get('description')
    result = caption_generator(description)
    return jsonify(result)

@app.route('/generate-prompt', methods=['POST'])
def prompt_generator():
    data = request.json
    user_info = data.get('user_info')
    result = prompt_generator(user_info)
    return jsonify(result)

@app.route('/view-image', methods=['POST'])
def check_status():
    data = request.json
    generation_id = data.get('generation_id')
    api_key = data.get('api_key')
    result = check_status(generation_id, api_key)
    return jsonify(result)

@app.route('/get-image-urls', methods=['POST'])
def get_image_urls():
    data = request.json
    generation_id = data.get('generation_id')
    api_key = data.get('api_key')
    result = get_image_urls(generation_id, api_key)
    return jsonify(result)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
