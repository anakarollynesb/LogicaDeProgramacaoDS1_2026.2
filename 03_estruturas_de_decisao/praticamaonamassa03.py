# TODO: Implemente o menu utilizando match-case ou elif
# Desenvolva a estrutura de seleção aqui

opcao = int(input("Digite a opção desejada (1, 2 ou 3): "))
match opcao: 
    case 1:
        print("Opção 01-Consultar livro")
    case 2:
        print("Opção 02-Realizar empréstimos")
    case 3:
        print ("Opção 03-Devolver livros")
    case _:
        print ("Opção Inválida!")
