# TODO: Defina a função calcular_media e teste-a abaixo
#def calcular_media(nota1, nota2, nota3):
    # Escreva o corpo da função
    #pass

# Teste com notas de exemplo

nota1 = float(input("Digite sua primeira nota:"))
nota2 = float(input("Digite sua segunda nota:"))
nota3 = float(input("Por fim, Digite sua terceira nota:"))
def calcular_media(nota1, nota2, nota3):
    media = (nota1 + nota2 + nota3)/3
    return media 
media = calcular_media(nota1, nota2, nota3)
print (f"Sua média é {media:.1f}")