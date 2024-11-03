# leonardo_service.py
import requests
import time
from app.utils.config import LEONARDO_API_KEY

def generate_image(request_text):
    url = "https://cloud.leonardo.ai/api/rest/v1/generations"
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "authorization": f"Bearer {LEONARDO_API_KEY}"
    }

    # prompt = prompt_text + ".\n" + user_request
    
    payload = {
        "alchemy": True,
        "height": 768,
        "modelId": "6b645e3a-d64f-4341-a6d8-7a3690fbf042", 
        "num_images": 4,
        "presetStyle": "DYNAMIC",
        "prompt": request_text,
        "width": 1024
    }
    
    response = requests.post(url, json=payload, headers=headers)
    return response.json()

def poll_for_image_links(id_image, max_attempts=10, wait_time=5):
    url = f"https://cloud.leonardo.ai/api/rest/v1/generations/{id_image}"
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "authorization": f"Bearer {LEONARDO_API_KEY}"
    }

    for attempt in range(max_attempts):
        response = requests.get(url, headers=headers)
        data = response.json()
        images = data.get("generations_by_pk", {}).get("generated_images", [])
        
        if images:
            return [img["url"] for img in images]
        
        time.sleep(wait_time)

    return []
