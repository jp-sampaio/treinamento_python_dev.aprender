# Range (Gerandores)
# O range serve para gerar valores de acordo com a faixa de valores que foi passada para ele

print(range(39))
print(type(range(39)))

# Sintaxes range(valor inicial, valor final, pulo)

for numero in range(1, 38, 2):
    print(numero)

# Gerando listas de formas mais faceis 

listas_de_numeros = list(range(2, 200, 5))
print(listas_de_numeros)