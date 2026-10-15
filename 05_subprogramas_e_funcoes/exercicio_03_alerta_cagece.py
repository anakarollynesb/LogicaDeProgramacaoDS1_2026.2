"""
EXERCÍCIO 03: Gerador de Alertas da Cagece
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Desenvolva um procedimento `emitir_alerta_fatura(nome_cliente, valor, data_vencimento)`
que imprima a mensagem:
"Prezado(a) [nome], sua fatura da Cagece no valor de R$ [valor] vence no dia [data]."
"""

# TODO: Desenvolva o procedimento abaixo:
nome = input (("Qual o seu nome?"))
valoR = input (("Qual o valor da sua fatura?"))
datA = input (("Qual a data de vencimento?"))
def emitir_alerta_fatura(nome_cliente, valor, data_vencimento):
    print (f"Prezado(a) {nome_cliente}, sua fatura da Cagece no valor de R$ {valor} vence no dia {data_vencimento}")
emitir_alerta_fatura(nome, valoR, datA)