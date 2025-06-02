from interface.menu import exibir_menu
from dados.persistencia import carregar_dados
from modelos.Livro import Livro
from modelos.Usuario import Usuario
from modelos.Emprestimo import Emprestimo
from datetime import datetime

# Função para converter datas em strings e reconvertê-las (para Emprestimo)
def str_para_data(data_str):
    return datetime.strptime(data_str, "%Y-%m-%d").date()

# Reconstrói os objetos Livro, Usuario e Emprestimo a partir dos dicionários
def reconstruir_livros(lista):
    return [Livro(**l) for l in lista]

def reconstruir_usuarios(lista):
    return [Usuario(**u) for u in lista]

def reconstruir_emprestimos(lista):
    emprestimos = []
    for e in lista:
        emprestimo = Emprestimo(
            e["usuario_id"],
            e["livro_id"],
            str_para_data(e["data_emprestimo"]),
            str_para_data(e["data_prevista"]),
            str_para_data(e["data_devolucao"]) if e["data_devolucao"] else None
        )
        emprestimos.append(emprestimo)
    return emprestimos

def main():
    # Carrega os dados dos arquivos JSON
    livros_json = carregar_dados("dados/livros.json")
    usuarios_json = carregar_dados("dados/usuarios.json")
    emprestimos_json = carregar_dados("dados/emprestimos.json")

    # Reconstrói os objetos a partir dos dados carregados
    livros = reconstruir_livros(livros_json)
    usuarios = reconstruir_usuarios(usuarios_json)
    emprestimos = reconstruir_emprestimos(emprestimos_json)

    # Inicia o sistema com os dados carregados
    exibir_menu(livros, usuarios, emprestimos)

if __name__ == "__main__":
    main()