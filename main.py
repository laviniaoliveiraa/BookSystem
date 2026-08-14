livros = []

def cadastrar():
    titulo = str(input("Diga o título do livro: "))
    autor = str(input("Diga o nome do autor: "))
    ano = int(input("Diga o ano de publicação: "))
    codigo_isbn = str(input("Digite o código ISBN do livro: "))
    status = "disponivel"
    livro = {
        "titulo": titulo,
        "autor": autor,
        "ano": ano,
        "isbn": codigo_isbn,
        "status": status,
    }
    livros.append(livro)


def emprestar():
    codigo_isbn = str(input("Diga o código ISBN do livro: "))
    for livro in livros:
        if livro["isbn"] == codigo_isbn:
            if livro["status"] == "disponivel":
                livro["status"] = "emprestado"
                print("Livro emprestado com sucesso")
            elif livro["status"] == "emprestado":
                print("Esse livro já foi emprestado")
            return
    print("Livro não encontrado")


def devolucao():
    codigo_isbn = str(input("Digite o código ISBN do livro: "))
    for livro in livros:
        if livro["isbn"] == codigo_isbn:
            if livro["status"] == "emprestado":
                livro["status"] = "disponivel"
                print("Livro devolvido com sucesso")
            elif livro["status"] == "disponivel":
                print("Esse livro não estava emprestado")
            return
    print("Livro não encontrado")


def listar():
    if livros == []:
        print("Nenhum livro cadastrado")
        return
    for livro in livros:
        print("Título:", livro["titulo"])
        print("Autor:", livro["autor"])
        print("Ano:", livro["ano"])
        print("Código ISBN:", livro["isbn"])
        print("Status:", livro["status"])
        print("------------------------------")


def buscar():
    while True:
        print("-------CAMPO DE BUSCA-------")
        print("1- Buscar por título")
        print("2- Buscar por autor")
        print("3- Voltar")
        opcao = int(input("Escolha uma opcao: "))
        if opcao == 3:
            break
        termo = str(input("Digite o termo que deseja buscar: "))
        encontrou = False
        for livro in livros:
            if opcao == 1 and livro["titulo"] == termo:
                print("Título:", livro["titulo"])
                print("Autor:", livro["autor"])
                print("Ano:", livro["ano"])
                print("Código ISBN:", livro["isbn"])
                print("Status:", livro["status"])
                encontrou = True
            if opcao == 2 and livro["autor"] == termo:
                print("Título:", livro["titulo"])
                print("Autor:", livro["autor"])
                print("Ano:", livro["ano"])
                print("Código ISBN:", livro["isbn"])
                print("Status:", livro["status"])
                encontrou = True
        if encontrou == False:
            print("Nenhum livro encontrado")


def ordenar():
    print("1- Ordenar por título")
    print("2- Ordenar por autor")
    print("3- Ordenar por Ano")
    opcao = int(input("Escolha uma opção: "))
    if opcao == 1:
        campo = "titulo"
    elif opcao == 2:
        campo = "autor"
    elif opcao == 3:
        campo = "ano"

    tamanho = len(livros)
    for i in range(tamanho):
        menor = i
        for j in range(i + 1, tamanho):
            if livros[j][campo] < livros[menor][campo]:
                menor = j
        livros[i], livros[menor] = livros[menor], livros[i]
    print("Lista ordenada com sucesso")


def salvar_livros():
    arquivo = open("livros.csv", "w")
    for livro in livros:
        arquivo.write(livro["titulo"])
        arquivo.write(",")
        arquivo.write(livro["autor"])
        arquivo.write(",")
        arquivo.write(str(livro["ano"]))
        arquivo.write(",")
        arquivo.write(livro["isbn"])
        arquivo.write(",")
        arquivo.write(livro["status"])
        arquivo.write("\n")
    arquivo.close()


def carregar_livros():
    arquivo = open("livros.csv", "r")
    for linha in arquivo:
        linha = linha.strip()
        dados = linha.split(",")
        livro = {
            "titulo": dados[0],
            "autor": dados[1],
            "ano": int(dados[2]),
            "isbn": dados[3],
            "status": dados[4]
        }
        livros.append(livro)
    arquivo.close()


def menu_principal():
    while True:
        print("-------MENU PRINCIPAL-------")
        print("1- Cadastrar")
        print("2- Emprestar")
        print("3- Devolução")
        print("4- Listar")
        print("5- Buscar")
        print("6- Ordenar")
        print("7- Sair")
        opcao = int(input("Digite a opção escolhida: "))
        if opcao == 1:
            cadastrar()
            salvar_livros()
        elif opcao == 2:
            emprestar()
            salvar_livros()
        elif opcao == 3:
            devolucao()
            salvar_livros()
        elif opcao == 4:
            listar()
        elif opcao == 5:
            buscar()
        elif opcao == 6:
            ordenar()
        elif opcao == 7:
            break


carregar_livros()
menu_principal()