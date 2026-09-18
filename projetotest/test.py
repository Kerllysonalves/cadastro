print("Olá, mundo!")

produtos = []
# FUNÇÃO PARA CADASTRAR PRODUTOS
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
# FUNÇÃO PARA LISTAR PRODUTOS
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

# FUNÇÃO PARA ALTERAR PREÇOS
def alterar_preco():
    print("\n---ALTERAR PREÇO---")
    nome_pesquisado = input("Pesquisar produto: ")

    for produto in produtos:
        if produto["nome"].lower() == nome_pesquisado.lower():

            print(f"Produto encontrado: {produto['nome']}")
            print(f"Preço atual: R$ {produto['preco_kg']:.2f}")

            novo_preco =float(input("Digite o novo valor do kg: "))

            produto["preco_kg"] = novo_preco

            print("Preço alterado com sucesso!")
            return

while True:
    print("\n===AÇOUGUE===")
    print("1- Cadastrar produto")
    print("2- Listar produto")
    print("3- Alterar preço")
    print("4- Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrar_produtos()

    elif opcao ==  "2":
        listar_produtos()

    elif opcao == "3":
        alterar_preco()

    elif opcao == "4":
        print("Programa encerrado.")
        break
    
    else:
        print("Opção inválida.")
    
