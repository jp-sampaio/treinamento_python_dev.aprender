"""
    COMO CRIAR E MODIFICAR ARQUIVOS 
    'w' -> Usado somente para escrita
    'a' -> Usado para acrescentar algo
    'r' -> Usado somente para leitura 
    'r+' -> Usado para ler e escrever algo
"""

import os

# Escrita 
with open('celulares.txt', 'w') as file: 
    file.write('Celular 2') # Ele vai subscrever sempre que for adicionado um novo texto

# Acrescentar algo
with open('celulares.txt', 'a', newline='') as file:
    file.write(os.linesep + 'Celular 5')

# Acrescentar varios nomes
nomes = ['lucas', 'carol', 'jeff', 'douglas']
with open('nomes.txt', 'w', newline='') as file:
    for nome in nomes:
        file.write(nome + os.linesep)

# Acrescentar varios numeros
numeros = [56, 23, 45, 30, 21]
with open('numeros.txt', 'w', newline='') as file:
    for numero in numeros:
        file.write(str(numero) + os.linesep)


# Leitura 
with open('nomes.txt', 'r') as file:
    # print(file.read())
    for linha in file:
        print(linha)


# Leitura e escrita 
with open('numeros.txt', 'r+') as file:
    for numero in file:
        print(numero)
    file.write('9000')        