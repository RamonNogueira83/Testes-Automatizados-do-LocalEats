VALOR_MINIMO_PEDIDO = 30.0


def pedido_atingiu_valor_minimo(valor_pedido):
    if valor_pedido < 0:
        raise ValueError("O valor do pedido nao pode ser negativo.")

    return valor_pedido >= VALOR_MINIMO_PEDIDO
