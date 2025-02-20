import requests
import base64
from app.config import settings

GEMINI_VISION_API_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro-vision:generateContent"

def encode_image(image_path):
    """Converte imagem para base64 para enviar para a API."""
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")

def identify_ingredients(image_path):
    """Usa Gemini Vision API para identificar ingredientes em uma imagem."""
    headers = {"Content-Type": "application/json"}
    params = {"key": settings.GEMINI_API_KEY}
    
    # Converte a imagem para base64
    image_base64 = encode_image(image_path)

    # Prompt para detecção de ingredientes
    prompt = """
    Você é um assistente culinário com visão computacional.
    Identifique quais ingredientes estão presentes na imagem enviada.
    Liste apenas os nomes dos ingredientes, sem descrições adicionais.
    """

    data = {
        "contents": [{
            "role": "user",
            "parts": [
                {"text": prompt},
                {"inline_data": {
                    "mime_type": "image/jpeg",
                    "data": image_base64
                }}
            ]
        }]
    }

    response = requests.post(GEMINI_VISION_API_URL, headers=headers, params=params, json=data)
    
    if response.status_code == 200:
        result = response.json()
        return result["candidates"][0]["content"]["parts"][0]["text"]
    else:
        return f"Erro: {response.json()}"
