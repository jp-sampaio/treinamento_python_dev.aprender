frase = 'Olá, bem-vindo a este treinamento!'
# print(frase.split()) # Separa por espaços em uma lista
# print(frase.split(',')) # Separa somente onde tem a vírgula
# print(frase.split('-')) # Separa somente onde tem o traço

nomes = 'joão, marcos, lucas, bruna, carla,luiza'
# print(nomes.split()) # Separa por espaços em uma lista
# print(nomes.split(',')) # Separa somente onde tem a vírgula

hashtags = 'music #guitar #gamer #coder #python'
# print(hashtags.split()) # Separa por espaços em uma lista
# print(hashtags.split('#')) # Separa somente onde tem a hashtag
# print(hashtags.split('#', 3)) # Separa somente onde tem a hashtag e 3 separações

# Como concatenar strings
hashtags_separadas_por_espaco = hashtags.split(' ')
# print(hashtags_separadas_por_espaco)
# print(','.join(hashtags_separadas_por_espaco)) # Junta a lista em uma string separada por vírgula
# print('.'.join(hashtags_separadas_por_espaco)) # Junta a lista em uma string separada por ponto
# print(' '.join(hashtags_separadas_por_espaco)) # junta a lista em uma string separada por espaço

'''
  Desafios:
  1- Transforme a frase_1 em uma lista de palavras e guarde o resultado em uma variável chamada palavra_1
  2- Transforme a frase_2 em uma lista de palavras e guarde o resultado em uma variável chamada palavra_2
  3- Pegue a palavra_1 e transforme elas no seguinte string: "Desafio,manipulação,de,strings". Imprima o resultado no console
  4- Pegue a palavra_2 e transforme elas no seguinte string: "jhonatan & rafael & carol & camilla". Imprima o resultado no console
'''
frase_1 = 'Desafio manipulação de strings'
frase_2 = 'jhonatan,rafael,carol,camilla'

palavra_1 = frase_1.split()
palavra_2 = frase_2.split(',')

# Desafio 1
print(palavra_1)
# Desafio 2
print(palavra_2)
# Desafio 3
print(','.join(palavra_1))
# Desafio 4
print(' & '.join(palavra_2))