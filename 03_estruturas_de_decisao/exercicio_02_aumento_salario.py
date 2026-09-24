"""
EXERCÍCIO 02: Aumento de Salário Escolar
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Leia o salário de um colaborador da escola e aplique o percentual de reajuste:
- 0.00 a 400.00: 15%
- 400.01 a 800.00: 12%
- 800.01 a 1200.00: 10%
- 1200.01 a 2000.00: 7%
- Acima de 2000.00: 4%

Imprima: novo salário, valor do reajuste ganho e percentual aplicado.
"""

# TODO: Desenvolva o algoritmo abaixo:

salario = float(input("Digite seu salário abaixo:"))
if salario<=400.00:
    reajuste = (salario*0.15)
    novoSalario = salario + reajuste
    print(f"Seu novo salário é {novoSalario}! Houve um reajuste de {reajuste} = 15%")
elif salario<=800:
    reajuste = salario*0.12
    novoSalario = salario + reajuste
    print(f"Seu novo salário é {novoSalario}! Houve um reajuste de {reajuste} = 12%")
elif salario<=1200:
    reajuste = salario*0.10
    novoSalario = salario + reajuste
    print(f"Seu novo salário é {novoSalario}! Houve um reajuste de {reajuste} = 10%")
elif salario<=2000:
    reajuste = salario*0.07
    novoSalario = salario + reajuste
    print(f"Seu novo salário é {novoSalario}! Houve um reajuste de {reajuste} = 7%")
else:
    reajuste = salario*0.04
    novoSalario = salario + reajuste
    print(f"Seu novo salário é {novoSalario}! Houve um reajuste de {reajuste} = 4%")

    #salario>2000
    #reajuste = salario*0.04
    #novoSalario = salario + reajuste
    #print(f"Seu novo salário é {novoSalario}! Houve um reajuste de {reajuste} = 4%")


