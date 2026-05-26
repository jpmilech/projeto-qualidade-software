import pytest
from pedido import calcular_total_pedido

def test_deve_calcular_total_quando_valor_minimo_atingido():
    itens = [{"preco": 10}, {"preco": 20}]
    valor_minimo = 15

    resultado = calcular_total_pedido(itens, valor_minimo)

    assert resultado == 30

def test_deve_retornar_total_exato_do_pedido():
    itens = [{"preco": 25}, {"preco": 15}]
    valor_minimo = 40

    resultado = calcular_total_pedido(itens, valor_minimo)

    assert resultado == 40

def test_deve_gerar_erro_quando_valor_minimo_nao_atingido():
    itens = [{"preco": 10}, {"preco": 5}]
    valor_minimo = 30

    with pytest.raises(ValueError):
        calcular_total_pedido(itens, valor_minimo)