from src.logic import (
    validar_horario, 
    calcular_proxima_dose, 
    buscar_endereco, 
    salvar_agendamento, 
    listar_agendamentos, 
    __version__
)

def menu():
    print("-" * 40)
    print(f"💊 MedManager CLI - v{__version__} (Cloud Edition)")
    print("-" * 40)
    print("1 - Cadastrar novo agendamento")
    print("2 - Listar agendamentos salvos na nuvem")
    opcao = input("\nEscolha uma opção: ")

    if opcao == "2":
        print("\nBuscando dados no banco de dados...")
        dados = listar_agendamentos()
        if not dados:
            print("Nenhum dado encontrado ou banco desconectado.")
        else:
            for d in dados:
                print(f"💊 {d.get('medicamento', 'Desconhecido')} | Próxima dose: {d.get('proxima_dose', 0):02d}:00h | CEP: {d.get('cep', 'N/A')}")
        return

    if opcao != "1":
        print("❌ Opção inválida.")
        return
    
    try:
        cep = input("\nCEP do paciente (apenas números): ")
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
        
        print("Sincronizando com a nuvem...")
        sucesso = salvar_agendamento(cep, nome_remedio, hora_inicial, intervalo, proxima)
        if sucesso:
            print("☁️ Dados salvos com sucesso no Supabase!")
        else:
            print("⚠️ Aviso: Rodando localmente. Configure as variáveis de ambiente para salvar na nuvem.")
            
    except ValueError as e:
        print(f"❌ Erro de entrada: {e}")

if __name__ == "__main__":
    menu()
