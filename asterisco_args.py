# Quando eu peciso de um valor mais flexível nos meus argumentos eu utilixo o asterisco no argumento e cria uma tupla com diferentes valores

def somar(*valores, soma):
    print(valores)
    for valor in valores:
        soma += valor
    print(soma)

somar(34, 26, 17, 10, soma=8)

# O argumento que não possui o asterisco deve ser nomeado como é o caso do soma = 8