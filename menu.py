livros = []

def cadastrar_livro():
    livro = input("Digite o nome do livro: ")
    autor = input("Nome do autor: ")
    npag = int(input("Número de páginas: "))

    livrocad = {
        "nome": livro,
        "autor": autor,
        "npag": npag
    }
    livros.append(livrocad)

#cadastrar_livro()

def lista_livros():
    print("\n---LIVROS CADASTRADOS---")

    if len(livros) == 0:
        print("Nenhum livro cadastrado.")
        return

    for livrocad in livros:
        print(
            f"Livro: {livrocad['nome']} "
            f"Autor: {livrocad['autor']} "
            f"Número de páginas: {livrocad['npag']} "
        )

    
while True:
    print("\n===BIBLIOTECA===")
    print("1- Cadastrar livro")
    print("2- Lista de livros")
    print("3- Sair")

    opcao = input("Escolha uma opção:")

    if opcao == "1":
        cadastrar_livro()

    elif opcao == "2":
        lista_livros()

    elif opcao == "3":
        print("Programa encerrado")
        break

    else:
        print("Opção inválida")


    

    