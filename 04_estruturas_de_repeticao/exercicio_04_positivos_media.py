"""
EXERCÍCIO 04: Positivos e Média
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Leia 6 valores numéricos.
Conte quantos foram estritamente positivos (> 0) e calcule a média aritmética deles.
Imprima a quantidade de positivos e a média formatada com 1 casa decimal.
"""

# TODO: Desenvolva o algoritmo abaixo:

contador = 0 
soma = 0
for i in range(6):
    valor = int (input("Digite o valor:"))
    if valor > 0:
        contador+=1
        soma+=valor 
        media = soma/contador 
print (f"A quantidade de números positivos é {contador}; e a média do mesmos é {media:.1f}")