def calcular_valor(sabor, tamanho):
    """Calcula o valor do pedido com base no sabor e tamanho."""
    preços = {
        "CP": {"P": 10, "M": 15, "G": 19},
        "AC": {"P": 12, "M": 17, "G": 21}
    }
    return preços[sabor][tamanho]