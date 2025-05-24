# servicos/biblioteca_service.py

from datetime import datetime, timedelta
from modelos.Emprestimo import Emprestimo

# Função para cadastrar um novo livro
def cadastrar_livro(livros, Livro):
    print("\n--- Cadastro de Livro ---")
    titulo = input("Título: ")
    autor = input("Autor: ")
    isbn = input("ISBN: ")
    ano = input("Ano de publicação: ")
    quantidade = int(input("Quantidade disponível: "))
    livro = Livro(titulo, autor, isbn, ano, quantidade)
    livros.append(livro)
    print("Livro cadastrado com sucesso.")

# Função para cadastrar um novo usuário
def cadastrar_usuario(usuarios, Usuario):
    print("\n--- Cadastro de Usuário ---")
    nome = input("Nome: ")
    matricula = input("Matrícula: ")
    curso = input("Curso: ")
    usuario = Usuario(nome, matricula, curso)
    usuarios.append(usuario)
    print("Usuário cadastrado com sucesso.")

# Função para realizar empréstimo com validações
def realizar_emprestimo(usuarios, livros, emprestimos):
    print("\n--- Empréstimo de Livro ---")
    matricula = input("Matrícula do usuário: ")
    usuario = encontrar_usuario(usuarios, matricula)

    if not usuario:
        print("Usuário não encontrado.")
        return

    # Regra: Máximo de 3 livros por usuário
    emprestimos_usuario = [e for e in emprestimos if e.usuario_id == matricula and e.data_devolucao is None]
    if len(emprestimos_usuario) >= 3:
        print("Usuário já atingiu o limite de 3 empréstimos.")
        return

    isbn = input("ISBN do livro: ")
    livro = encontrar_livro(livros, isbn)

    if not livro:
        print("Livro não encontrado.")
        return

    # Regra: Só emprestar se houver exemplares
    if livro.quantidade <= 0:
        print("Não há exemplares disponíveis.")
        return

    # Registrar empréstimo
    data_emprestimo = datetime.now().date()
    data_prevista = data_emprestimo + timedelta(days=7)
    emprestimo = Emprestimo(matricula, isbn, data_emprestimo, data_prevista)
    emprestimos.append(emprestimo)
    livro.quantidade -= 1
    print(f"Empréstimo realizado. Devolver até {data_prevista}.")

# Função para realizar devolução com verificação de atraso
def realizar_devolucao(livros, emprestimos):
    print("\n--- Devolução de Livro ---")
    matricula = input("Matrícula do usuário: ")
    isbn = input("ISBN do livro: ")

    for e in emprestimos:
        if e.usuario_id == matricula and e.livro_id == isbn and e.data_devolucao is None:
            e.data_devolucao = datetime.now().date()
            livro = encontrar_livro(livros, isbn)
            if livro:
                livro.quantidade += 1
            if e.data_devolucao > e.data_prevista:
                print("Livro devolvido com atraso.")
            else:
                print("Livro devolvido no prazo.")
            return

    print("Empréstimo não encontrado ou já devolvido.")

# Função para exibir os relatórios
def exibir_relatorios(livros, emprestimos):
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

# Função utilitária para buscar um usuário por matrícula
def encontrar_usuario(usuarios, matricula):
    return next((u for u in usuarios if u.matricula == matricula), None)

# Função utilitária para buscar um livro por ISBN
def encontrar_livro(livros, isbn):
    return next((l for l in livros if l.isbn == isbn), None)