## 🛠️ Prática do Aluno (Mão na Massa)
# TODO: Desenvolva seu algoritmo aqui
# 1. Leia o valor da conta (float)
# 2. Leia o número de pessoas (int)
# 3. Calcule o valor por pessoa
# 4. Imprima formatado usando f-string

valor_da_compra = float(input("digite o valor da compra:R$"))
numero_de_pessoas = int(input ("numero de pessoas:"))
valor_por_pessoa = valor_da_compra / numero_de_pessoas

print(f"O valor final por pessoa é R$ {valor_por_pessoa:.1f}")

