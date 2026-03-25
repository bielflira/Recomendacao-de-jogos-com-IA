from fastapi import FastAPI
from routes import auth, games, recommend

app = FastAPI()

app.include_router(auth.router)
app.include_router(games.router)
app.include_router(recommend.router)

@app.get("/")
def root():
    return {"msg": "GameAI rodando 🚀"}
