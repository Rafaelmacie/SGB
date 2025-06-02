from datetime import datetime, timedelta
from modelos.Emprestimo import Emprestimo
from dados.persistencia import salvar_tudo  # <- Importa persistência

# Função para cadastrar um novo livro
def cadastrar_livro(livros, Livro, usuarios, emprestimos):
    print("\n--- Cadastro de Livro ---")
    titulo = input("Título: ")
    autor = input("Autor: ")
    isbn = input("ISBN: ")
    ano = input("Ano de publicação: ")
    quantidade = int(input("Quantidade disponível: "))
    livro = Livro(titulo, autor, isbn, ano, quantidade)
    livros.append(livro)
    print("Livro cadastrado com sucesso.")
    salvar_tudo(livros, usuarios, emprestimos)  # <- Salva após cadastro

# Função para cadastrar um novo usuário
def cadastrar_usuario(usuarios, Usuario, livros, emprestimos):
    print("\n--- Cadastro de Usuário ---")
    matricula = input("Matrícula: ")

    if any(u.matricula == matricula for u in usuarios):
        print("Já existe um usuário com essa matrícula.")
        return

    nome = input("Nome: ")
    curso = input("Curso: ")
    usuario = Usuario(nome, matricula, curso)
    usuarios.append(usuario)
    print("Usuário cadastrado com sucesso.")
    salvar_tudo(livros, usuarios, emprestimos)

# Empréstimo pelo administrador
def realizar_emprestimo(usuarios, livros, emprestimos):
    print("\n--- Empréstimo de Livro ---")
    matricula = input("Matrícula do usuário: ")
    usuario = encontrar_usuario(usuarios, matricula)

    if not usuario:
        print("Usuário não encontrado.")
        return

    emprestimos_usuario = [e for e in emprestimos if e.usuario_id == matricula and e.data_devolucao is None]
    if len(emprestimos_usuario) >= 3:
        print("Usuário já atingiu o limite de 3 empréstimos.")
        return

    isbn = input("ISBN do livro: ")
    livro = encontrar_livro(livros, isbn)

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
    salvar_tudo(livros, usuarios, emprestimos)

# Devolução pelo administrador
def realizar_devolucao(livros, emprestimos, usuarios):
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
            salvar_tudo(livros, usuarios, emprestimos)
            return

    print("Empréstimo não encontrado ou já devolvido.")

# Relatórios
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

# Empréstimo pelo próprio usuário
def realizar_emprestimo_usuario(usuario, livros, emprestimos, usuarios):
    print("\n--- Empréstimo de Livro ---")
    emprestimos_usuario = [e for e in emprestimos if e.usuario_id == usuario.matricula and e.data_devolucao is None]
    if len(emprestimos_usuario) >= 3:
        print("Você já atingiu o limite de 3 empréstimos.")
        return

    isbn = input("ISBN do livro: ")
    livro = next((l for l in livros if l.isbn == isbn), None)

    if not livro:
        print("Livro não encontrado.")
        return

    if livro.quantidade <= 0:
        print("Não há exemplares disponíveis.")
        return

    data_emprestimo = datetime.now().date()
    data_prevista = data_emprestimo + timedelta(days=7)
    emprestimo = Emprestimo(usuario.matricula, isbn, data_emprestimo, data_prevista)
    emprestimos.append(emprestimo)
    livro.quantidade -= 1
    print(f"Empréstimo realizado. Devolver até {data_prevista}.")
    salvar_tudo(livros, usuarios, emprestimos)

# Devolução pelo próprio usuário
def realizar_devolucao_usuario(usuario, livros, emprestimos, usuarios):
    print("\n--- Devolução de Livro ---")
    isbn = input("ISBN do livro: ")
    for e in emprestimos:
        if e.usuario_id == usuario.matricula and e.livro_id == isbn and e.data_devolucao is None:
            e.data_devolucao = datetime.now().date()
            livro = next((l for l in livros if l.isbn == isbn), None)
            if livro:
                livro.quantidade += 1
            if e.data_devolucao > e.data_prevista:
                print("Livro devolvido com atraso.")
            else:
                print("Livro devolvido no prazo.")
            salvar_tudo(livros, usuarios, emprestimos)
            return
    print("Nenhum empréstimo ativo encontrado para este livro.")

# Função para buscar um usuário por matrícula
def encontrar_usuario(usuarios, matricula):
    return next((u for u in usuarios if u.matricula == matricula), None)

# Função para buscar um livro por ISBN
def encontrar_livro(livros, isbn):
    return next((l for l in livros if l.isbn == isbn), None)