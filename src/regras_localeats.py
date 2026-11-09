# Responsavel: Ramon Nogueira.

VALOR_MINIMO_PEDIDO = 30.0


def pedido_atingiu_valor_minimo(valor_pedido):
    if valor_pedido < 0:
        raise ValueError("O valor do pedido nao pode ser negativo.")

    return valor_pedido >= VALOR_MINIMO_PEDIDO

# Responsavel: Alessandro Reis da Silva.

def quantidade_itens_valida(quantidade):
    if quantidade >= 1 and quantidade <= 10:
        return True
    elif quantidade < 0:
        raise ValueError("Não existe quantidade negativa.")
    else:
        return False