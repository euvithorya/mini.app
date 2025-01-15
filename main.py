from organizador import adicionar_compromisso, listar_compromissos, buscar_compromissos_por_data
from datetime import datetime 

def exibir_menu():
    print("\nOrganizador de Horários")
    print("1. Adicionar compromisso")
    print("2. Listar compromissos")
    print("3. Buscar compromissos por data")
    print("4. Sair")

def validar_data(data):
    """Valida se a data está no formato correto (AAAA-MM-DD)."""
    try:
        datetime.strptime(data, "%Y-%m-%d")
        return True
    except ValueError:
        return False

def main():
    while True:
        exibir_menu()
        escolha = input("Escolha uma opção: ")
        if escolha == "1":
            data = input("Digite a data do compromisso (AAAA-MM-DD): ")
            if validar_data(data):
                descricao = input("Digite a descrição do compromisso: ")
                print(adicionar_compromisso(data, descricao))
            else:
                print("Formato de data inválido. Use o formato AAAA-MM-DD.")
        elif escolha == "2":
            print("\nCompromissos:")
            print(listar_compromissos())
        elif escolha == "3":
            data = input("Digite a data para buscar (AAAA-MM-DD): ")
            if validar_data(data):
                print("\nResultados:")
                print(buscar_compromissos_por_data(data))
            else:
                print("Formato de data inválido. Use o formato AAAA-MM-DD.")
        elif escolha == "4":
            print("Saindo... Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()

#:V