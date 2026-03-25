import requests

API_KEY = "SUA_CHAVE"

def buscar_jogos():
    url = f"https://api.rawg.io/api/games?key={API_KEY}"
    res = requests.get(url).json()
    return res["results"]
