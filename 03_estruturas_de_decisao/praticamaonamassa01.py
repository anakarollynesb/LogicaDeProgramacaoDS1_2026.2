# Crie a variável aprovado com a expressão lógica
from encodings.punycode import T


aprovado = None # Substitua None pela expressão lógica
print("Status de aprovação:", aprovado)

media_aluno = float(input("digite sua media(0-10):"))
frequencia_percentual = float (input("digite sua frequencia percentual(0-100):"))
reprovado = (media_aluno<6.0) and (frequencia_percentual<75)
aprovado = (media_aluno>=6.0) and (frequencia_percentual>=75)
if  (media_aluno>=6.0) and (frequencia_percentual>=75):
    print (f"Status de aprovacao: Aprovado")
else:   print ("Status de aprovacao:Reprovado") 

