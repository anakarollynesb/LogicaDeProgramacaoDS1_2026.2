"""
EXERCÍCIO 02: Resto da Divisão por 5
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Leia dois valores inteiros X e Y.
Utilize o laço for para imprimir todos os inteiros entre X e Y (em ordem crescente)
cujo resto da divisão por 5 seja igual a 2 ou igual a 3.
"""

# TODO: Desenvolva o algoritmo abaixo:

valor1 = int(input("Digite o primeiro valor(X):"))
valor2 = int(input("Digite o segundo valor(Y):"))
for numero in range (valor1, valor2 + 1):
    if numero % 5 == 2 or numero % 5 == 3:
        print(numero)
