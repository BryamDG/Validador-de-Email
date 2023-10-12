import re

def validar_email(email):
    padrao = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    
    if re.match(padrao, email):
        return True
    else:
        return False

endereco_email = input("Digite um endereço de e-mail: ")

if validar_email(endereco_email):
    print("E-mail válido.")
else:
    print("E-mail inválido.")
