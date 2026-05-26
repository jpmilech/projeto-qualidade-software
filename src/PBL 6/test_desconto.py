import pytest
from desconto import aplicar_desconto

def test_deve_aplicar_desconto_percentual_corretamente():
    resultado = aplicar_desconto(100, 10)

    assert resultado == 90

def test_deve_retornar_valor_sem_desconto():
    resultado = aplicar_desconto(200, 0)

    assert resultado == 200

def test_deve_gerar_erro_para_desconto_invalido():
    with pytest.raises(ValueError):
        aplicar_desconto(100, 150)