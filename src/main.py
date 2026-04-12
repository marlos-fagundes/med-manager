from logic import validar_horario, calcular_proxima_dose, __version__

def menu():
    print("-" * 30)
    print(f"MedManager CLI - v{__version__}")
    print("Controle de Medicamentos")
    print("-" * 30)
    
    try:
        nome_remedio = input("Nome do medicamento: ")
        hora_inicial = int(input("Hora da primeira dose (0-23): "))
        
        if not validar_horario(hora_inicial):
            print("❌ Erro: A hora deve estar entre 0 e 23.")
            return

        intervalo = int(input("Intervalo entre doses (em horas): "))
        
        proxima = calcular_proxima_dose(hora_inicial, intervalo)
        
        print("\n" + "=" * 30)
        print(f"✅ Agendamento para: {nome_remedio}")
        print(f"⏰ Próxima dose às: {proxima:02d}:00h")
        print("=" * 30)
        
    except ValueError:
        print("❌ Erro: Por favor, digite apenas números inteiros para horários e intervalos.")

if __name__ == "__main__":
    menu()
