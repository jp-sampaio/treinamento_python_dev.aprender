# Valores aleatórios com random
import random

# print(random.random()) # Gera valores aleatórios entre 0.0 á 1.0
# print(random.uniform(4, 10)) # Gera umm valor decimal de valor minimo e de valor maximo
# print(random.randint(4, 10)) # Gera umm valor inteiro de valor minimo e de valor maximo

# colors = ['red', 'green', 'blue', 'orange', 'yellow']
# # Escolher um valor aleatório dentro dessa lista
# print(random.choices(colors))

# cards_from_a_deck = ['latter_1', 'latter_2', 'latter_3', 'latter_4', 'latter_5']
# #  Embaralhar as cartas da lista
# print(random.shuffle(cards_from_a_deck))

# print(cards_from_a_deck)



# ​​DESAFIO 🥇
# Desafios Random 
# 1. Você quer simular a opção de jogar uma moeda e resultar em cara ou coroa
# jogue as opções dentro de uma variável e depois crie um programa que imprimir 'cara' ou 'coroa' na tela

cara_ou_coroa = ['cara', 'coroa']
print(random.choice(cara_ou_coroa))

# 2. Você quer fazer um sorteio entre 5 nomes em uma lista de nomes
# Crie uma lista de 5 nomes e sorteie um nome de dentro dessa lista e exiba na tela

nomes = ['marcos', 'paulo', 'manoela', 'fernanda', 'mirela']
nome_embaralhado = random.shuffle(nomes)
print(random.choice(nome_embaralhado))

# 3. você quer escolher aleatóriamente um número de 10-100
# Imprima na tela um valor aleatório entre 10 e 100

valor_aleatorio = random.randint(10, 100)
print(valor_aleatorio)