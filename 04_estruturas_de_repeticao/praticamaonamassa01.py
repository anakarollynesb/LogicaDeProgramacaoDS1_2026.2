# TODO: Implemente a tabuada aqui
#numero = int(input("Digite um número para ver a tabuada: "))

# Escreva o laço for

numero_base = int (input("Digite um número para ver a tabuada:"))
for numero in range (1,11):
    tabuada = numero_base*numero
    print (f"{numero}x{numero_base} = {tabuada}")