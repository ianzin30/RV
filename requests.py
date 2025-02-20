import requests

url = "http://127.0.0.1:8000/image/upload/"

# Abrir e enviar a imagem
with open("teste.jpg", "rb") as img_file:
    files = {"file": img_file}
    response = requests.post(url, files=files)

# Exibir resposta
print(response.json())
