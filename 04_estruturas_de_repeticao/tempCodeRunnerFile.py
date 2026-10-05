senha_correta = "2002"
while True:
    tentativa = input("Digite a senha de acesso: ")
    if tentativa == senha_correta:
        print("Acesso Permitido!")
        break
    else:
        print("Senha Inválida!")
        continue