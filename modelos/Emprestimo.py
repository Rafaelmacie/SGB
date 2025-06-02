from datetime import datetime, date

class Emprestimo:
    def __init__(self, usuario_id, livro_id, data_emprestimo, data_prevista, data_devolucao=None):
        # Garante que os atributos de data estejam no tipo correto (datetime.date)

        self.usuario_id = usuario_id
        self.livro_id = livro_id

        # Converte string para date, se necessário
        self.data_emprestimo = self._converter_para_data(data_emprestimo)
        self.data_prevista = self._converter_para_data(data_prevista)
        self.data_devolucao = self._converter_para_data(data_devolucao) if data_devolucao else None

    # Método auxiliar para conversão de string para datetime.date
    def _converter_para_data(self, valor):
        if isinstance(valor, date):
            return valor
        if isinstance(valor, str):
            return datetime.strptime(valor, "%Y-%m-%d").date()
        raise ValueError("Valor de data inválido")
