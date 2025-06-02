import json
import os
from datetime import date

# Carrega dados de um arquivo JSON, retornando uma lista de dicionários
def carregar_dados(caminho):
    if os.path.exists(caminho):
        with open(caminho, 'r', encoding='utf-8') as arquivo:
            return json.load(arquivo)
    return []

# Salva dados (lista de dicionários) em um arquivo JSON
def salvar_dados(caminho, dados):
    with open(caminho, 'w', encoding='utf-8') as arquivo:
        json.dump(dados, arquivo, indent=4, ensure_ascii=False)

# Salva todos os dados de uma vez (livros, usuários e empréstimos)
def salvar_tudo(livros, usuarios, emprestimos):
    from modelos.Livro import Livro
    from modelos.Usuario import Usuario
    from modelos.Emprestimo import Emprestimo

    # Salva livros e usuários diretamente, pois usam apenas tipos simples
    salvar_dados("dados/livros.json", [l.__dict__ for l in livros])
    salvar_dados("dados/usuarios.json", [u.__dict__ for u in usuarios])

    # Converte datas em string para os empréstimos
    emprestimos_dict = []
    for e in emprestimos:
        emprestimos_dict.append({
            "usuario_id": e.usuario_id,
            "livro_id": e.livro_id,
            "data_emprestimo": e.data_emprestimo.isoformat() if isinstance(e.data_emprestimo, date) else e.data_emprestimo,
            "data_prevista": e.data_prevista.isoformat() if isinstance(e.data_prevista, date) else e.data_prevista,
            "data_devolucao": e.data_devolucao.isoformat() if isinstance(e.data_devolucao, date) else None
        })

    salvar_dados("dados/emprestimos.json", emprestimos_dict)