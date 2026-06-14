import os
import requests
from supabase import create_client

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

def get_supabase_client():
    url = os.environ.get("SUPABASE_URL")
    key = os.environ.get("SUPABASE_KEY")
    if url and key:
        return create_client(url, key)
    return None

def salvar_agendamento(cep, remedio, hora_inicial, intervalo, proxima):
    """Escreve os dados no Supabase (Create)"""
    db = get_supabase_client()
    if db:
        try:
            db.table('agendamentos').insert({
                "cep": cep,
                "medicamento": remedio,
                "hora_inicial": hora_inicial,
                "intervalo": intervalo,
                "proxima_dose": proxima
            }).execute()
            return True
        except Exception:
            return False
    return False

def listar_agendamentos():
    """Lê os dados do Supabase (Read)"""
    db = get_supabase_client()
    if db:
        try:
            res = db.table('agendamentos').select("*").execute()
            return res.data
        except Exception:
            return []
    return []
