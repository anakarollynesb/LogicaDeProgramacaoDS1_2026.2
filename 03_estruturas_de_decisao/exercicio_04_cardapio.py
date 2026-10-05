"""
EXERCÍCIO 04: Cardápio da Lanchonete
Disciplina: Lógica de Programação com Python

TABELA:
1 - Cachorro Quente: R$ 4.00
2 - X-Salada: R$ 4.50
3 - X-Bacon: R$ 5.00
4 - Torrada Simples: R$ 2.00
5 - Refrigerante: R$ 1.50

ENUNCIADO:
Leia o código do item e a quantidade consumida.
Calcule e mostre o total a pagar.
"""

# TODO: Desenvolva o algoritmo abaixo:

codigo = float (input("Digite o código do item(1-5): "))
quantidadeConsumida = float(input("Digite a quantidade consumida:"))
cachorroQuente = 4.50
XSalada=4.50
XBacon=5.00
TorradaSimples=2.00
Refrigerante=1.50
if codigo==1:
    totalPagar = (quantidadeConsumida*4.00)
    print(f"O total a ser pago é {totalPagar}")
elif codigo==2:
    totalPagar = (quantidadeConsumida*4.50)
    print(f"O total a ser pago é {totalPagar}")
elif codigo==3:
    totalPagar = (quantidadeConsumida*5.00)
    print(f"O total a ser pago é {totalPagar}")
elif codigo==4:
    totalPagar = (quantidadeConsumida*2.00)
    print(f"O total a ser pago é {totalPagar}")
elif codigo==5:
    totalPagar = (quantidadeConsumida*1.50)
    print(f"O total a ser pago é {totalPagar}")
else:
    print(f"Código Inválido!")
    exit()
