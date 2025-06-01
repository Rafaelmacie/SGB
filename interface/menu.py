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
    exibir_relatorios,
    realizar_emprestimo_usuario,
    realizar_devolucao_usuario,
)

# Estruturas de dados em memória
livros = []
usuarios = []
emprestimos = []

# Menu inicial de seleção de perfil
def exibir_menu():
    print("\n=== Bem-vindo ao Sistema de Gestão de Biblioteca ===")
    print("Logar como:")
    print("1. Administrador")
    print("2. Usuário comum")

    perfil = input("Escolha seu perfil (1 ou 2): ")

    if perfil == "1":
        verif_admin()
    elif perfil == "2":
        verif_user()
    else:
        print("Perfil inválido.")

def verif_admin():
    tentativas = 0
    admin = input("\nDigite seu nome: ")
    senhaAdmin = 123
    senha = 0

    while senha != senhaAdmin:
        senha = int(input("\nDigite sua senha: "))

        if senha != senhaAdmin:
            print("Senha incorreta")
            tentativas += 1

            if(tentativas == 3):
                print("\nLimite de tentativas excedido. O programa será finalizado")
                return
    
    print(f"\nBem-vindo, {admin}!")
    menu_administrador()
    return

def verif_user():
    matricula = input("\nDigite sua matrícula: ")
    usuario = next((u for u in usuarios if u.matricula == matricula), None)

    if usuario:
        print(f"\nBem-vindo, {usuario.nome}!")
    else:
        print("\nUsuário não encontrado. Vamos realizar seu cadastro.")
        cadastrar_usuario(usuarios, Usuario)
        usuario = usuarios[-1]  # Último usuário cadastrado
        print("Cadastro concluído.")

    # Passa o usuário logado para o menu do usuário
    menu_usuario(usuario)


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
            print("\nEncerrando o sistema.")
            exit()
        else:
            print("Opção inválida.")

# Menu restrito ao usuário comum
def menu_usuario(usuario_logado):
    while True:
        print(f"\n--- Menu do Usuário: {usuario_logado.nome} ---")
        print("1. Realizar Empréstimo")
        print("2. Realizar Devolução")
        print("3. Voltar ao menu inicial")
        print("0. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            realizar_emprestimo_usuario(usuario_logado, livros, emprestimos)
        elif opcao == "2":
            realizar_devolucao_usuario(usuario_logado, livros, emprestimos)
        elif opcao == "3":
            return exibir_menu()
        elif opcao == "0":
            print("\nEncerrando o sistema.")
            exit()
        else:
            print("Opção inválida.")
