"""
EXERCÍCIO 03: Fórmula de Bhaskara
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Leia 3 valores de ponto flutuante (A, B e C) de uma equação do 2º grau.
- Se A for 0 ou delta for negativo, imprima "Impossivel calcular".
- Caso contrário, calcule e mostre as duas raízes (R1 e R2) formatadas com 5 casas decimais.
"""

# TODO: Desenvolva o algoritmo abaixo:
import math

valorA =float (input("Insira o valor de(a): "))
valorB =float (input("Insira o valor de(b): "))
valorC =float (input("Insira o valor de(c): "))
delta = (valorB**2)-(4*valorA*valorC)
if valorA == 0 or delta<0 :
    print("Impossível calcular")
else:
    raiz1 = (-valorB+math.sqrt(delta))/(2*valorA)
    raiz2 = (-valorB-math.sqrt(delta))/(2*valorA)
    print(f"As raízes da fórmula são {raiz1:.5f} e {raiz2:.5f}")
