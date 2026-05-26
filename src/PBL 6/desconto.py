def aplicar_desconto(valor_total, desconto):
    if desconto < 0 or desconto > 100:
        raise ValueError("Desconto inválido")

    valor_final = valor_total - (valor_total * desconto / 100)

    if valor_final < 0:
        raise ValueError("Valor final inválido")

    return valor_final