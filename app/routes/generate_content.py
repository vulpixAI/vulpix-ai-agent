from services.gemini_service import generate_caption
from services.leonardo_service import generate_image, poll_for_image_links

def generate_content(prompt, user_request):
    image_data = generate_image(prompt, user_request)
    generation_id = image_data.get("sdGenerationJob", {}).get("generationId")

    if not generation_id:
        return {"error": "Failed to obtain generation ID"}

    #pega o link das imagens usando polling
    image_urls = poll_for_image_links(generation_id)

    #gera legenda usando o user_request
    caption = generate_caption(user_request)

    return {
        "image_urls": image_urls,
        "caption": caption
    }
