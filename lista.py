# Listas servem para armazenar mais de uma informação em uma espaço.
precos = [10, 20, 30]
print(precos[2]) # 30 - Acessa o valor pelo indice
print(precos.index(20)) # 1 - Descobrir o indice do numero 20 na lista

# Listas no python são dinâmicas (aceitam qualquer tipo de dado)
itens = [1, 3, 6, 'Olá', 'café', True, 10.76]
print(itens[4]) # Café

# Maneiras diferentes de gerar uma lista
# Multiplicação de valores(repetição)
lista_de_noves = [9] * 10
lista_de_testes = ['teste'] * 10
print(lista_de_noves) # Imprime 9 dez vezes
print(lista_de_testes) # Imprime teste dez vezes

# Usando o gerador range (Sequência)
# 0 até 29
faixa_de_numeros = list(range(30))
print(faixa_de_numeros)

# Gerar a partir de strings
string_desmembrada = list('Bem-vindo ao treinamento')
print(string_desmembrada)

# Lista de lista (Matriz)
matriz_de_nomes = [['Carol', 30], ['Marcus', 50]]
print(matriz_de_nomes[0]) # ['Carol', 30]
print(matriz_de_nomes[0][0]) # Carol
print(matriz_de_nomes[1][0]) # Marcus



# ========================= Desafio ================================
# Desafios 🥇

# Desafio #1 Crie uma lista que tenha os nomes dos 3 objetos que você mais usa durante o dia e imprima ele na tela
# Desafio #2 Usando apenas uma linha de código, crie uma lista de 10 a 131
# Desafio #3 Imprima na tela o resultado da combinação da lista do desafio 1 e desafio 2
# Desafio #4 Crie uma lista de listas(matriz) que tenha os nomes dos 3 objetos
#  que você mais usa durante o dia, mas agora dentro de cada item você vai colocar 
# uma informação extra, coloque o valor em reais desse objeto também e imprima ele 
# na tela  

objetos_favoritos = ['Celular', 'Computador', 'Ventilador']
print(objetos_favoritos)

lista_de_numeros = list(range(10, 132))
print(lista_de_numeros)

print(objetos_favoritos + lista_de_numeros)

objetos_favoritos_precificados = [['Celular', 1500], ['Computador', 6300], ['Ventilador', 100]]
print(objetos_favoritos_precificados)