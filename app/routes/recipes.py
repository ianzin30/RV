from fastapi import APIRouter
from app.services.gemini_service import get_recipe_from_gemini

router = APIRouter(prefix="/recipes", tags=["Recipes"])

@router.get("/{ingredients}")
async def get_recipe_suggestions(ingredients: str):
    """Recebe ingredientes e retorna sugestões de receitas usando Gemini."""
    recipes = get_recipe_from_gemini(ingredients)
    return {"recipes": recipes}
