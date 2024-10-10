from flask import Flask, request, jsonify
from app.generate_image import image_generator
from app.generate_caption import caption_generator
from app.generate_prompt import prompt_generator

app = Flask(__name__)

@app.route('/generate-image', methods=['POST'])
def image_generation():
    data = request.json
    prompt = data.get('prompt')
    model_id = data.get('model_id')
    result = image_generator(prompt, model_id)
    return jsonify(result)

@app.route('/generate-caption', methods=['POST'])
def caption_generation():
    data = request.json
    description = data.get('description')
    result = caption_generator(description)
    return jsonify(result)

@app.route('/generate-prompt', methods=['POST'])
def prompt_generation():
    data = request.json
    user_info = data.get('user_info')
    result = prompt_generator(user_info)
    return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
