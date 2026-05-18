import pytest
from src.logic import validar_horario, calcular_proxima_dose, buscar_endereco

def test_horario_valido():
    assert validar_horario(10) is True

def test_calculo_proxima_dose():
    assert calcular_proxima_dose(22, 8) == 6

def test_integracao_viacep_valido():
    # Teste de integração real batendo em um serviço externo
    resultado = buscar_endereco("01001000")
    assert resultado is not None
    assert "Praça da Sé" in resultado

def test_integracao_viacep_invalido():
    with pytest.raises(ValueError):
        buscar_endereco("123")
