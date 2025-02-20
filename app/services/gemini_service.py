import requests
from app.config import settings

GEMINI_API_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent"

def get_recipe_from_gemini(ingredients: str):
    """Gera receitas usando o Gemini API com regras específicas."""
    headers = {"Content-Type": "application/json"}
    params = {"key": settings.GEMINI_API_KEY}

    # Melhorando o prompt para garantir restrições nos ingredientes
    prompt = f"""
    Você é um assistente culinário especializado em criar receitas.
    
    **Regras:**
    - Use exclusivamente os seguintes ingredientes: {ingredients}.
    - Não adicione nenhum outro ingrediente.
    - Inclua um passo a passo claro e detalhado.
    - Se necessário, sugira variações, mas sempre usando apenas os ingredientes fornecidos.
    - Retorne a resposta de forma estruturada: primeiro a lista de ingredientes, depois o modo de preparo.

    Agora, crie uma receita completa usando apenas os ingredientes mencionados.
    """

    data = {
        "contents": [{
            "role": "user",
            "parts": [{"text": prompt}]
        }]
    }

    response = requests.post(GEMINI_API_URL, headers=headers, params=params, json=data)
    
    if response.status_code == 200:
        result = response.json()
        return result["candidates"][0]["content"]["parts"][0]["text"]
    else:
        return f"Erro: {response.json()}"
