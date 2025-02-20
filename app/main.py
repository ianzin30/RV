from fastapi import FastAPI
from app.routes import recipes, image_processing

app = FastAPI(title="Déja Food API", version="1.0")

app.include_router(recipes.router)
app.include_router(image_processing.router)

@app.get("/")
def read_root():
    return {"message": "Déja Food API is running!"}
