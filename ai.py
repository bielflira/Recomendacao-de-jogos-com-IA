def explicar(jogo, recomendados):
    respostas = []

    for rec in recomendados:
        texto = f"Se você gostou de {jogo}, vai curtir {rec['name']} por ter mecânicas e estilo semelhantes."
        respostas.append(texto)

    return respostas
