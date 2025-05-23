def exibir_menu():
    while True:
        print("\n--- Sistema de Gestão de Biblioteca ---")
        print("1. Cadastrar Livro")
        print("2. Cadastrar Usuário")
        print("3. Realizar Empréstimo")
        print("4. Realizar Devolução")
        print("5. Relatórios")
        print("0. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "0":
            print("Encerrando o sistema.")
            break
        else:
            print(f"Opção {opcao} ainda não implementada.")