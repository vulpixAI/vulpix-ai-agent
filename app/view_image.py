import requests
import os 
from dotenv import load_dotenv

load_dotenv()

LEONARDO_API_KEY = os.getenv("LEONARDO_API_KEY")

class LeonardoStatusChecker:
    def __init__(self, generation_id, api_key):
        self.generation_id = generation_id
        self.headers = {
            "accept": "application/json",
            "content-type": "application/json",
            "authorization": f"Bearer {api_key}"
        }

    def check_status(self):
        status_url = f"https://cloud.leonardo.ai/api/rest/v1/generations/{self.generation_id}"
        response = requests.get(status_url, headers=self.headers)
        return response.json()

    def get_image_urls(self):
        data = self.check_status()
        images = data.get("generations_by_pk", {}).get("generated_images", [])
        return [img.get("url") for img in images] if images else []

checker = LeonardoStatusChecker("ec103d6d-2473-4dfb-b380-8ca1b7a27aa2", "75839dd1-02b8-45c0-b33d-96e44c7c44ff")
image_urls = checker.get_image_urls()
for url in image_urls:
    print(url)
