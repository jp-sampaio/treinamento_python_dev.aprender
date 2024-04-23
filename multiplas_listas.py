# Trabalhando comm multiplas listas
# Importando a biblioteca que vai proporcionar trabalhar com listas de tamanhos diferentes
from itertools import zip_longest

a_lista = ['A', 'B', 'C', 'D', 'E']
b_lista = [1, 2, 3, 4, 5]

for a, b in zip(a_lista, b_lista):
    print(a)
    print(b)

produtos = ['produto1', 'produto2', 'produto3', 'produto4', 'produto5']
precos = [250, 150, 220, 550, 50]

for produto, preco in zip(produtos, precos):
    print(f'Salvando {produto} que custa R${preco}')


# Passando por listas com tamanhos diferentes

titulos = ['titulo1', 'titulo2', 'titulo3', 'titulo4', 'titulo5']
descricoes = ['descrição1', 'descrição2', 'descrição3']

for titulo, descricao in zip_longest(titulos, descricoes):
    print(f'Encontramos o {titulo} com {descricao}')


#  ================ Desafio ===========================
    
# DESAFIOS 🥇

## DESAFIO 1

# Usando as listas abaixo:

products = ['Produto 1', 'Produto 2', 'Produto 3', 'Produto 4', 'Produto 5']

prices = ['R$500,00', 'R$1500,00', 'R$2700,00', 'R$5000,00']

# Estamos extraindo preços de um site de produtos e queremos armazenar as informações encontradas, porém a pesquisa foi encontrada em momentos diferentes, 
# assim acabamos com duas listas diferentes, favor criar uma mensagem que diz o nome e valor produto, como as mensagens abaixo:

for product, price in zip_longest(products, prices):
    print(f'Produto: {product} encontrado no valor de R${price}')

# Produto: Produto 1 encontrado no valor de R$500,00

# Produto: Produto 2 encontrado no valor de R$1500,00

# Produto: Produto 3 encontrado no valor de R$2700,00

# Produto: Produto 4 encontrado no valor de R$5000,00

# Produto: Produto 5 encontrado no valor de None  