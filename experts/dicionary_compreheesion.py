# Funciona de maneira muito similar a list compreheesion 
# Sintaxe => {chave: expressão for membro in iteravel}

from pprint import pprint
import random

pprint({i: i for i in range(5)})

products = ['produto 1', 'produto 2', 'produto 3', 'produto 4', 'produto 5']
# Imprimir os produtos como chave e o seu indice como valor
pprint({product: str(products.index(product) + 1) for product in products})
# Imprimir uma matriz com 5 números 0 com product como valor 
pprint({product: [0 for i in range(5)] for product in products})
# Imprimir o dobro dos números que iram ser passados 
pprint({product: [i * 2 for i in range(5)] for product in products})
# Imprimir números aleatórios que iram ser valores da chave product
pprint({product: [random.randint(100, 1000) for i in range(4)] for product in products})

