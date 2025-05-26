# SGB
Um sistema de gestão de bibliotecas feito com arquitetura monolítica

# MANUAL

Ao iniciar o sistema é apresentado duas opções, "1" para o administrador e "2" para um usuário comum.

---No menu do Administrador você tem as seguintes opções:

1. Cadastrar Livro
2. Cadastrar Usuário
3. Realizar Empréstimo
4. Realizar Devolução
5. Relatórios
6. Voltar ao menu inicial
0. Sair

Ao digitar algum dos números você ira realizar a ação que foi solicitada.

---No menu do usuário comum você tem as seguintes opções:

1. Cadastrar Usuário
2. Realizar Empréstimo
3. Realizar Devolução
4. Voltar ao menu inicial
0. Sair

Assim como o administrador o usuário comum pode realizar ações, porém, existe restrições em que o usuário comum não é permitido.

Cada funcionalidade tem por finalidade fazer com que ocorra o que foi escrito no número solicitado.


# Demonstração de algumas funcionalidades:

Ao iniciar o sistema e selecionar a opção 1, é direcionado para o menu do administrador, para cadastrar um livro é preciso selecionar a opção 1.

Ao solicitar a cadastrar vai ser solicitado as seguintes informações:

Título: 
Autor: 
ISBN: 
Ano de publicação: 
Quantidade disponível:

Após isso o livro ja vai estar cadastrado com sucesso.
------------------------------------------------------------------------------------

Para cadastrar um usuário comum(2) funciona da mesma forma no menu do administrador, as seguintes informações a serem preenchidas são:

Nome:
Matrícula:
Curso:

Após isso o usuário vai ser cadastrado com sucesso 

------------------------------------------------------------------------------------

Para a realização de empréstimos de livro(3) vão ser solicitados os seguintes dados:

Matrícula do usuário: 
ISBN do livro: 

------------------------------------------------------------------------------------

Após todos esse procedimentos de algumas funcionalidades, o livro cadastrado e solicitado, e usuário cadstrado foram:

--- Cadastro de Livro --- Opção 1
Título: O pequeno príncipe 
Autor: Antoine de Saint-Exupéry
ISBN: 8595081514
Ano de publicação: 1943
Quantidade disponível: 10
Livro cadastrado com sucesso.

--- Cadastro de Usuário --- Opção 2
Nome: Erlano
Matrícula: 12345
Curso: ADS
Usuário cadastrado com sucesso.

--- Empréstimo de Livro --- Opção 3
Matrícula do usuário: 12345
ISBN do livro: 8595081514
Empréstimo realizado. Devolver até 2025-06-01.

--- Relatórios --- Opção 5

Livros emprestados:
Usuário: 12345, Livro: 8595081514, Previsto: 2025-06-01