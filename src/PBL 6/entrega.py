def calcular_taxa_entrega(distancia):
    if distancia < 0:
        raise ValueError("Distância inválida")

    if distancia <= 3:
        return 5

    return 5 + (distancia - 3) * 2