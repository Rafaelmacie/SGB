from modelos.Livro import Livro
from modelos.Usuario import Usuario
from modelos.Emprestimo import Emprestimo
from datetime import datetime, timedelta

livros = []
usuarios = []
emprestimos = []

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
            cadastrar_livro()
        elif opcao == "2":
            cadastrar_usuario()
        elif opcao == "3":
            realizar_emprestimo()
        elif opcao == "4":
            realizar_devolucao()
        elif opcao == "5":
            exibir_relatorios()
        elif opcao == "6":
            return exibir_menu()
        elif opcao == "0":
            print("Encerrando o sistema.")
            exit()
        else:
            print("Opção inválida.")

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
            cadastrar_usuario()
        elif opcao == "2":
            realizar_emprestimo()
        elif opcao == "3":
            realizar_devolucao()
        elif opcao == "4":
            return exibir_menu()
        elif opcao == "0":
            print("Encerrando o sistema.")
            exit()
        else:
            print("Opção inválida.")

def cadastrar_livro():
    print("\n--- Cadastro de Livro ---")
    titulo = input("Título: ")
    autor = input("Autor: ")
    isbn = input("ISBN: ")
    ano = input("Ano de publicação: ")
    quantidade = int(input("Quantidade disponível: "))
    livro = Livro(titulo, autor, isbn, ano, quantidade)
    livros.append(livro)
    print("Livro cadastrado com sucesso.")

def cadastrar_usuario():
    print("\n--- Cadastro de Usuário ---")
    nome = input("Nome: ")
    matricula = input("Matrícula: ")
    curso = input("Curso: ")
    usuario = Usuario(nome, matricula, curso)
    usuarios.append(usuario)
    print("Usuário cadastrado com sucesso.")

def realizar_emprestimo():
    print("\n--- Empréstimo de Livro ---")
    matricula = input("Matrícula do usuário: ")
    usuario = encontrar_usuario(matricula)
    if not usuario:
        print("Usuário não encontrado.")
        return

    emprestimos_usuario = [e for e in emprestimos if e.usuario_id == matricula and e.data_devolucao is None]
    if len(emprestimos_usuario) >= 3:
        print("Usuário já atingiu o limite de 3 empréstimos.")
        return

    isbn = input("ISBN do livro: ")
    livro = encontrar_livro(isbn)
    if not livro:
        print("Livro não encontrado.")
        return

    if livro.quantidade <= 0:
        print("Não há exemplares disponíveis.")
        return

    data_emprestimo = datetime.now().date()
    data_prevista = data_emprestimo + timedelta(days=7)
    emprestimo = Emprestimo(matricula, isbn, data_emprestimo, data_prevista)
    emprestimos.append(emprestimo)
    livro.quantidade -= 1
    print(f"Empréstimo realizado. Devolver até {data_prevista}.")

def realizar_devolucao():
    print("\n--- Devolução de Livro ---")
    matricula = input("Matrícula do usuário: ")
    isbn = input("ISBN do livro: ")
    for e in emprestimos:
        if e.usuario_id == matricula and e.livro_id == isbn and e.data_devolucao is None:
            e.data_devolucao = datetime.now().date()
            livro = encontrar_livro(isbn)
            if livro:
                livro.quantidade += 1
            if e.data_devolucao > e.data_prevista:
                print("Livro devolvido com atraso.")
            else:
                print("Livro devolvido no prazo.")
            return
    print("Empréstimo não encontrado ou já devolvido.")

def exibir_relatorios():
    print("\n--- Relatórios ---")
    print("\nLivros emprestados:")
    for e in emprestimos:
        if e.data_devolucao is None:
            print(f"Usuário: {e.usuario_id}, Livro: {e.livro_id}, Previsto: {e.data_prevista}")

    print("\nUsuários com empréstimos atrasados:")
    hoje = datetime.now().date()
    for e in emprestimos:
        if e.data_devolucao is None and e.data_prevista < hoje:
            print(f"Usuário: {e.usuario_id}, Livro: {e.livro_id}, Previsto: {e.data_prevista}")

    print("\nLivros disponíveis:")
    for l in livros:
        if l.quantidade > 0:
            print(f"{l.titulo} (ISBN: {l.isbn}) - {l.quantidade} disponíveis")

def encontrar_usuario(matricula):
    return next((u for u in usuarios if u.matricula == matricula), None)

def encontrar_livro(isbn):
    return next((l for l in livros if l.isbn == isbn), None)