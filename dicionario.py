# Dicionários
# Sintaxes é a chave e o valor

# Formas de se criar um dicionário
pessoa1 = {'nome': 'João', 'idade': 87, 'altura': 1.60}
pessoa2 = dict(nome= 'Julia', idade= 15, altura= 1.80)

# Formas de acessar os valores e chaves do dicionario
print(pessoa2['nome']) # Utiliza a chave para acessar o valor

# Acessar as chaves
chaves = pessoa1.keys()
print(chaves)
for chave in chaves:
    print(chave)

# Acessar os valores
valores = pessoa1.values()
print(valores)
for valor in valores:
    print(valor)

# Acessar todos os valores e chaves 
itens = pessoa2.items()
print(itens)

for item in itens:
    print(item)
    print(item[1])