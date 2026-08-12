def menu_principal():
    while True:
    print("-------Menu Principal-------")
    print("1 - CADASTRAR")
    print("2 - EMPRESTAR")
    print("3 - DEVOLUÇÃO")
    print("4 - LISTAR")
    print("5 - BUSCAR")
    print("6 - ORDENAR")
    print("7 - SAIR")
    opcao = int(input("Digite a opção escolhida: "))
    if opcao == 1:
    cadastrar()
elif opcao == 2:
    emprestar()
elif opcao == 3:
    devolucao()
elif opcao == 4:
    listar()
elif opcao == 5:
    buscar()
elif opcao == 6:
    ordenar()
elif opcao == 7:
    break
def cadastrar():
    titulo = str(input("Diga o título do livro: "))
    autor = str(input("Diga o autor do livro: "))
    ano = int(input("Diga o ano de publicação do livro: "))
    codigo_isbn = int(input("Diga o códido ISBN: "))
    status = "disponível"
    livro = {
        "titulo": titulo, 
        "autor": autor,
        "ano": ano,
        "isbn": codigo_isbn,
        "status": status,
        
    }
    livros.append(livro)
    
    


    


        
            

                    

            
                    
                    
                
