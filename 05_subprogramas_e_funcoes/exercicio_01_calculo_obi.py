"""
EXERCÍCIO 01: Pontuação OBI (Astro Lume Devs)
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Crie uma função nomeada `calcular_pontuacao_total(fase1, fase2, fase3)` com a diretiva `def`
que receba as 3 notas como parâmetros e retorne a pontuação total da equipe.
"""

# TODO: Desenvolva a função e os testes abaixo:
fase1 = float(input("Qual foi a pontuação na 1° fase?"))
fase2 = float(input("Qual foi a pontuação na 2° fase?"))
fase3 = float(input("Qual foi a pontuação na 3° fase?"))
def calcular_pontuacao_total(fase1, fase2, fase3):
    return fase1 + fase2 + fase3
pontuacao = calcular_pontuacao_total (fase1, fase2, fase3)
print ("A pontuação total da equipe é", pontuacao) 
