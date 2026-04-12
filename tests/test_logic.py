import pytest
from src.logic import validar_horario, calcular_proxima_dose

def test_horario_valido():
    assert validar_horario(10) is True
    assert validar_horario(25) is False

def test_entrada_invalida():
    with pytest.raises(ValueError):
        validar_horario("dez")

def test_calculo_proxima_dose():
    # Se tomou às 22h de 8 em 8 horas, a próxima é às 6h
    assert calcular_proxima_dose(22, 8) == 6
