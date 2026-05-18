import requests

__version__ = "1.0.0"

def validar_horario(hora):
    if not isinstance(hora, int):
        raise ValueError("A hora deve ser um número inteiro.")
    return 0 <= hora <= 23

def calcular_proxima_dose(hora_atual, intervalo):
    if intervalo <= 0:
        return None
    proxima = (hora_atual + intervalo) % 24
    return proxima

def buscar_endereco(cep):
    """Integração externa: Busca o endereço na API pública do ViaCEP."""
    cep = str(cep).replace("-", "").strip()
    if len(cep) != 8:
        raise ValueError("CEP inválido. Deve conter 8 dígitos.")

    url = f"https://viacep.com.br/ws/{cep}/json/"
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            dados = response.json()
            if "erro" in dados:
                return None
            return f"{dados.get('logradouro')}, {dados.get('bairro')} - {dados.get('localidade')}/{dados.get('uf')}"
    except requests.RequestException:
        return None
    return None
