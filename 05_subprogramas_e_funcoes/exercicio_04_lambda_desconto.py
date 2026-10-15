"""
EXERCÍCIO 04: Função Lambda de Desconto Casas Paulino
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Escreva uma função anônima (lambda) que receba o valor de um produto
e retorne o valor com 15% de desconto à vista aplicado.
"""

# TODO: Desenvolva a expressão lambda e teste-a abaixo:

valor_com_desconto = lambda v : v-(v*0.15)
v = float (input("Qual o valor do produto?"))
print (f"O valor do produto com desconto é {valor_com_desconto(v)}")
