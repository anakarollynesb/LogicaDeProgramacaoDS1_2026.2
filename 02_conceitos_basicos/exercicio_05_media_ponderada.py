"""
EXERCÍCIO 05: Média Ponderada da Avaliação Técnica
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Solicite as notas de três avaliações do curso técnico.
A primeira prova tem peso 2, a segunda peso 3 e a terceira peso 5.
Calcule e exiba a média final ponderada utilizando apenas operadores aritméticos.
"""

# TODO: Desenvolva o algoritmo abaixo:

nota1 = float(input("Digite a 1° Nota:"))
nota2 = float(input("Digite a 2° Nota:"))
nota3 = float (input("Digite a 3° Nota:"))
pesoNota1 = nota1*2
pesoNota2 = nota2*3
pesoNota3 = nota3*5

soma = pesoNota1+pesoNota2+pesoNota3
mediaFinal = soma / 10
print(f"A sua média final é {mediaFinal:.2f}")
