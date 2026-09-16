print("Olá, mundo!")

produtos = []

def cadastrar_produtos():
    print("---CADASTRO DE PRODUTOS---")

    nome = input("Digite o nome do produto: ")
    preco_kg = float(input("Preço por kg: "))

    produto = {
        "nome": nome,
        "preco_kg": preco_kg
    }

    produtos.append(produto)
    print("\nPRODUTO CADASTRADO COM SUCESSO!")

def listar_produtos():
    print("\n---PRODUTOS CADASTRADOS---")

    if len(produtos) == 0:
         print("Nenhum produto cadastrado.")
         return

    for produto in produtos:
        print(
        f"Produto: {produto['nome']} | "
        f"Valor do kg: R$ {produto['preco_kg']:.2f}"
    )

while True:
    print("\n===AÇOUGUE===")
    print("1- Cadastrar produto")
    print("2- Listar produto")
    print("3- Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrar_produtos()

    elif opcao ==  "2":
        listar_produtos()

    elif opcao == "3":
        print("Programa encerrado.")
        break

    else:
        print("Opção inválida.")
    
