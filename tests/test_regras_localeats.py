# Responsavel: Ramon Nogueira.

import pytest

from src.regras_localeats import pedido_atingiu_valor_minimo


def test_pedido_atinge_valor_minimo():
    assert pedido_atingiu_valor_minimo(50) is True
    assert pedido_atingiu_valor_minimo(30) is True


def test_pedido_abaixo_do_valor_minimo():
    assert pedido_atingiu_valor_minimo(20) is False


def test_pedido_com_valor_negativo():
    with pytest.raises(ValueError):
        pedido_atingiu_valor_minimo(-10)
