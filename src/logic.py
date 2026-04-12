__version__ = "1.0.0"

def validar_horario(hora):
    """Valida se a hora está entre 0 e 23."""
    if not isinstance(hora, int):
        raise ValueError("A hora deve ser um número inteiro.")
    return 0 <= hora <= 23

def calcular_proxima_dose(hora_atual, intervalo):
    """Calcula a próxima dose ignorando minutos para simplificação CLI."""
    if intervalo <= 0:
        return None
    proxima = (hora_atual + intervalo) % 24
    return proxima
