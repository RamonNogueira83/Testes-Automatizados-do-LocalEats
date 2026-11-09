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

# Responsavel: Alessandro Reis da Silva.

from src.regras_localeats import quantidade_itens_valida

def test_quatidade_de_itens_permitidos():
    assert quantidade_itens_valida(10) is True
    assert quantidade_itens_valida(1) is True
    assert quantidade_itens_valida(5) is True

def test_quatidade_de_itens_acima_do_permitido():
    assert quantidade_itens_valida(11) is False

def test_quatidade_de_itens_igual_a_zero():
    assert quantidade_itens_valida(0) is False

def test_quatidade_de_itens_negativos():
    with pytest.raises(ValueError):
        quantidade_itens_valida(-1)