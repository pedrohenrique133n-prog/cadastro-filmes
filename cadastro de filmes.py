filmes = []


def pedir_numero(mensagem):
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            print("Digite apenas números, por exemplo: 12")


while True:
    print("\n1 - Cadastrar filme")
    print("2 - Listar filmes")
    print("3 - Ver filmes liberados para minha idade")
    print("0 - Sair")
    opcao = input("Escolha: ")

    if opcao == "1":
        nome = input("Nome do filme: ")
        classificacao = pedir_numero("Classificação indicativa: ")
        filmes.append({"nome": nome, "classificacao": classificacao})
        print("Filme cadastrado!")

    elif opcao == "2":
        if not filmes:
            print("Nenhum filme cadastrado ainda.")
        for filme in filmes:
            print(filme["nome"], "-", filme["classificacao"], "anos")

    elif opcao == "3":
        idade = pedir_numero("Qual a sua idade? ")
        for filme in filmes:
            if idade >= filme["classificacao"]:
                print("Pode assistir:", filme["nome"])
            else:
                print("Não pode assistir:", filme["nome"])

    elif opcao == "0":
        break

    else:
        print("Opção inválida, tente de novo.")

        
         
