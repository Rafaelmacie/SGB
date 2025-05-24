# Importação das classes
from modelos.Livro import Livro
from modelos.Usuario import Usuario
from modelos.Emprestimo import Emprestimo

# Importação das regras de negócio organizadas
from servicos.biblioteca_service import (
    cadastrar_livro,
    cadastrar_usuario,
    realizar_emprestimo,
    realizar_devolucao,
    exibir_relatorios
)

# Estruturas de dados em memória
livros = []
usuarios = []
emprestimos = []

# Menu inicial de seleção de perfil
def exibir_menu():
    print("\n=== Bem-vindo ao Sistema de Gestão de Biblioteca ===")
    print("Você é:")
    print("1. Administrador")
    print("2. Usuário comum")

    perfil = input("Escolha seu perfil (1 ou 2): ")

    if perfil == "1":
        menu_administrador()
    elif perfil == "2":
        menu_usuario()
    else:
        print("Perfil inválido.")

# Menu exclusivo do administrador com todas as funcionalidades
def menu_administrador():
    while True:
        print("\n--- Menu do Administrador ---")
        print("1. Cadastrar Livro")
        print("2. Cadastrar Usuário")
        print("3. Realizar Empréstimo")
        print("4. Realizar Devolução")
        print("5. Relatórios")
        print("6. Voltar ao menu inicial")
        print("0. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_livro(livros, Livro)
        elif opcao == "2":
            cadastrar_usuario(usuarios, Usuario)
        elif opcao == "3":
            realizar_emprestimo(usuarios, livros, emprestimos)
        elif opcao == "4":
            realizar_devolucao(livros, emprestimos)
        elif opcao == "5":
            exibir_relatorios(livros, emprestimos)
        elif opcao == "6":
            return exibir_menu()
        elif opcao == "0":
            print("Encerrando o sistema.")
            exit()
        else:
            print("Opção inválida.")

# Menu restrito ao usuário comum
def menu_usuario():
    while True:
        print("\n--- Menu do Usuário ---")
        print("1. Cadastrar Usuário")
        print("2. Realizar Empréstimo")
        print("3. Realizar Devolução")
        print("4. Voltar ao menu inicial")
        print("0. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_usuario(usuarios, Usuario)
        elif opcao == "2":
            realizar_emprestimo(usuarios, livros, emprestimos)
        elif opcao == "3":
            realizar_devolucao(livros, emprestimos)
        elif opcao == "4":
            return exibir_menu()
        elif opcao == "0":
            print("Encerrando o sistema.")
            exit()
        else:
            print("Opção inválida.")