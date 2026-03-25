from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer('all-MiniLM-L6-v2')

def gerar_embeddings(jogos):
    textos = [j["name"] + " " + j.get("genres", [{}])[0].get("name","") for j in jogos]
    return model.encode(textos)

def recomendar(jogo_usuario, jogos, embeddings):
    idx = [j["name"] for j in jogos].index(jogo_usuario)

    similaridades = cosine_similarity([embeddings[idx]], embeddings)[0]

    indices = similaridades.argsort()[-6:][::-1]

    return [jogos[i] for i in indices if jogos[i]["name"] != jogo_usuario]
