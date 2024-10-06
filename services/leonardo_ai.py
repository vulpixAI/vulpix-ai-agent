import requests
import os

LEONARDO_API_KEY = os.getenv('LEONARDO_API_KEY')
BASE_URL = "https://cloud.leonardo.ai/api/rest/v1"

def get_headers():
    return {
        'Authorization': f'Bearer {LEONARDO_API_KEY}',
        'Content-Type': 'application/json',
    }

def get_user_info():
    url = f"{BASE_URL}/me"
    headers = get_headers()
    response = requests.get(url, headers=headers)
    return response.json()

user_info = get_user_info()
print(user_info)