from fastapi import APIRouter, UploadFile, File
from app.services.gemini_vision_service import identify_ingredients
import shutil
import os

router = APIRouter(prefix="/image", tags=["Image Processing"])

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)  # Criar pasta se não existir

@router.post("/upload/")
async def upload_image(file: UploadFile = File(...)):
    """Recebe uma imagem e identifica ingredientes usando Gemini Vision API."""
    file_path = f"{UPLOAD_FOLDER}/{file.filename}"
    
    # Salvar a imagem temporariamente
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Processar a imagem e identificar ingredientes
    ingredients = identify_ingredients(file_path)

    return {"ingredients": ingredients}
