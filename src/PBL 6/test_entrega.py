import pytest
from entrega import calcular_taxa_entrega

def test_taxa_fixa_ate_3km():
    assert calcular_taxa_entrega(2) == 5

def test_taxa_proporcional():
    assert calcular_taxa_entrega(5) == 9

def test_deve_gerar_erro_para_distancia_negativa():
    with pytest.raises(ValueError):
        calcular_taxa_entrega(-1)