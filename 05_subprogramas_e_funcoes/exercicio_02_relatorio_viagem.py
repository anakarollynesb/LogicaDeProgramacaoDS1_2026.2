"""
EXERCÍCIO 02: Modularizando Relatório de Viagem
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Crie duas funções:
1. `calcular_custo_transporte(distancia_km, consumo_kml, preco_combustivel)`
2. `calcular_custo_alimentacao(qtd_pessoas, dias, diaria_alimentacao)`

No programa principal, leia os dados, execute as funções e mostre o custo total da viagem.
"""

# TODO: Desenvolva as funções e o programa principal abaixo:

distancia = float (input("Qual a distância percorrida(Km)?"))
consumo = float (input("Qual o consumo em litros(Km/L)?"))
preco = float (input("Qual o preço do combustível(R$)?"))
def calcular_custo_transporte(distancia_km, consumo_kml, preco_combustivel):
    return (distancia_km/consumo_kml)*preco_combustivel
custo = calcular_custo_transporte(distancia, consumo, preco)

qtdPessoas = int (input("Qual a quantidade de pessoas?"))
dias = float (input("Serão quantos dias?"))
diaria = float (input("Quanto é a alimentação diária?"))
def calcular_custo_alimentacao(qtd_pessoas, dias, diaria_alimentacao):
    return (qtd_pessoas*dias)*diaria_alimentacao
custoAli = calcular_custo_alimentacao(qtdPessoas, dias, diaria)

custoTotal = custoAli+ custo

print("O custo do transporte é ", custo)
print("O custo em alimentação é ", custoAli)
print("O custo total é ", custoTotal)