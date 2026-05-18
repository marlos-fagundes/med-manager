from src.logic import validar_horario, calcular_proxima_dose, buscar_endereco, __version__

def menu():
    print("-" * 40)
    print(f"💊 MedManager CLI - v{__version__}")
    print("-" * 40)
    
    try:
        cep = input("CEP do paciente (apenas números): ")
        print("Buscando endereço na base nacional...")
        endereco = buscar_endereco(cep)
        
        if endereco:
            print(f"📍 Cadastrado em: {endereco}\n")
        else:
            print("⚠️ CEP não encontrado ou inválido. Prosseguindo sem endereço...\n")

        nome_remedio = input("Nome do medicamento: ")
        hora_inicial = int(input("Hora da primeira dose (0-23): "))
        
        if not validar_horario(hora_inicial):
            print("❌ Erro: A hora deve estar entre 0 e 23.")
            return

        intervalo = int(input("Intervalo entre doses (em horas): "))
        proxima = calcular_proxima_dose(hora_inicial, intervalo)
        
        print("\n" + "=" * 40)
        print(f"✅ Agendamento Confirmado: {nome_remedio}")
        print(f"⏰ Próxima dose às: {proxima:02d}:00h")
        print("=" * 40)
        
    except ValueError as e:
        print(f"❌ Erro de entrada: {e}")

if __name__ == "__main__":
    menu()
