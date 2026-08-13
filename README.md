# BookSystem
Esse é um sistema de gerenciamento de biblioteca desenvolvido em Python, que realiza o controle do acervo de livros de uma biblioteca, como o: cadastro, emprestimo, devolução, listagem, busca e ordem dos livros.

## Como executar o programa:
1. Se certificar de ter o Python instalado no computador 
2. Abrir o terminal na pasta do projeto
3. Executar o comando "python main.py"
4. O menu principal aparecerá no terminal, basta digitar o número da opção desejada e seguir as instruções.

## Funcionalidades

- **Cadastrar livros:** Registra um novo livro com (título, autor, ano de publicação, ISBN), com status inicial sempre "disponível"

- **Emprestar livros:** Busca o livro pelo ISBN e altera o status para "emprestado", caso ele esteja disponível

- **Devolução de livros:** Busca o livro pelo ISBN e altera o status de volta para "disponível", caso ele esteja emprestado

- **Listar livros:** Mostra todos os livros cadastrados, com todas as informações e o status atual de cada um

- **Buscar livros:** Permite procurar um livro pelo título ou pelo autor

- **Ordenar livros:** Reorganiza a lista de livros por título, autor ou ano de publicação.

- **Persistência em arquivo:** o catálogo de livros é salvo em arquivo (livros.csv) e recuperado automaticamente quando o programa é reaberto.

## Requisitos Técnicos Aplicados

- **Menu com if/elif/else:** usado na função menu_principal(), para direcionar cada opção escolhida pelo usuário para a função correspondente.

- **Estrutura de repetição (while):** usada em menu_principal(), mantendo o menu ativo até o usuário escolher a opção "sair".

- **Funções próprias com parâmetro e retorno:** usadas ao longo de todo o sistema, por exemplo nas funções responsáveis por cadastrar, buscar e ordenar os livros.

- **Lista de dicionários em memória:** os livros são armazenados na lista livros, onde cada livro é um dicionário com os campos título, autor, ano, ISBN e status.

- **Persistência de dados em arquivo:** o catálogo é salvo e lido do arquivo livros.csv, garantindo que os dados não se percam ao fechar o programa.