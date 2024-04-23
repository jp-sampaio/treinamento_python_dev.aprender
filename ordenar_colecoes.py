# Para ordenar as listas é preciso a importação da biblioteca itemgetter
from operator import itemgetter 

nomes = ['Zack', 'Camilla', 'Julius', 'Romer']
valores = [31, 23, 6, 36, 21, 33, 37, 7, 20, 23]
pessoas = [
    {
        'nome': 'John',
        'idade': 32,
        'nivel_acesso': 2
    },
    {
        'nome': 'Carol',
        'idade': 18,
        'nivel_acesso': 3
    },
    {
        'nome': 'Thomas',
        'idade': 45,
        'nivel_acesso': 3
    },
    {
        'nome': 'Amanda',
        'idade': 23,
        'nivel_acesso': 5
    }
]

pessoas.sort(key=itemgetter('idade')) # Ordenou os dicionários em ordem cresncente de acordo com as idades
print(pessoas)

# As tuplas e as listas são ordenadas pelo indice
produtos = [ 
    ('Celular', 750),
    ('Bicicleta', 1500),
    ('Microfone', 550)
]

produtos.sort(key=itemgetter(1)) # Ordena pelo indice mais 1 de cada tupla dentro da lista pelo indice 1 
print(produtos)

matriz = [[5, 10], [15, 21], [1, 5]]
matriz.sort(key=itemgetter(0), reverse=True) # Ordenar na ordem inversa pegando pelo indice 0 de cada lista dentro da lista
print(matriz)


# Ordene a lista de produtos abaixo pelo preço em ordem crescente
products = [
    {'nome': 'Celular',
     'preco': 1500
     },
    {'nome': 'Monitor',
     'preco': 500
     },
    {'nome': 'Microfone',
     'preco': 300
     }
]

products.sort(key=itemgetter('preco'))
print(products)


# Ordene em ordem descrescente a lista de equipamento_filmagem por valor do equipamento
equipamento_filmagem = [
    ('Tripé', 300),
    ('Câmera', 1700),
    ('Iluminação', 200),
]

equipamento_filmagem.sort(key=itemgetter(1), reverse=True)
print(equipamento_filmagem)

# Ordene em ordem crescente a cotacao_moedas com base no valor da moeda

cotacao_moedas = [['usd', 5.25], ['brl', 1.56], ['eur', 6.47]]

cotacao_moedas.sort(key=itemgetter(1))
print(cotacao_moedas)