"""
EXERCÍCIO 05: Acesso à Bilheteria do Parque
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Receba a idade do visitante (valor base do ingresso: R$ 100,00):
- Menor que 12 anos: "Infantil" (50% de desconto -> R$ 50,00)
- Maior ou igual a 60 anos: "Melhor Idade" (Gratuidade -> R$ 0,00)
- Demais idades: "Integral" (R$ 100,00)

Imprima o tipo de bilhete e o valor final a pagar.
"""

# TODO: Desenvolva o algoritmo abaixo:
print ("Acesso ao Parque-Valor do ingresso sem desconto: R$100,00")
idade = float(input("Digite a sua idade:"))
if idade<12:
    print ("Infantil-(50% de desconto -> R$ 50,00)")
elif idade>=60:
    print ("Melhor idade-(Gratuidade -> R$ 0,00)")
else:
    print ("Integral-R$100,00")
