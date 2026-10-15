"""
EXERCÍCIO 05: Gestão de Escopo Global e Local
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Declare a variável global total_inscritos = 0.
Crie a função `inscrever_aluno(quantidade)` utilizando a diretiva `global`
para atualizar a variável. Demonstre o valor de total_inscritos antes e depois da chamada.
"""

# TODO: Desenvolva o algoritmo abaixo:

total_inscritos = 0 
def inscrever_aluno(quantidade):
    global total_inscritos
    total_inscritos+=quantidade
    print (f"A quantidade de alunos inscritos é {total_inscritos} ")
quantidade = int(input("Qual a quantidade de alunos?"))
print(F"O total de inscritos antes da chamada é {total_inscritos}")
inscrever_aluno(quantidade)