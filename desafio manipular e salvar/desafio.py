# ​​ 🥇 DESAFIO Manipulação de Arquivos🥇
'''
    Veja o desafio, tente fazer por conta própria e depois veja a solução que estou passando aqui
    # Primeiro crie 3 listas
    * Uma lista que contem 5 frutas
    * Uma lista que contem 5 cores
    * Uma lista que contem 5 linguagens de programação
    # Desafio 1 - Crie um novo arquivo chamado frutas.txt e insira dentro dele todos as 5 frutas que estão na lista de frutas
    # Desafio 2 - Imprima na tela todas as linhas que estao dentro do arquivo frutas.txt
    # Desafio 3 - Sem apagar os dados que já estão dentro de frutas.txt, adicione todas as cores que estão dentro da sua lista de cores ao arquivos frutas.txt
    # Desafio 4 - Crie um novo arquivo chamado 'Top 5 Linguagens.txt' e popule o arquivo, de forma com que cada linuguagem ocupe apenas uma linha.
    # BONUS - Como você poderia criar vários arquivos diferentes usando um laço for e strings dinâmicos(f'{}'), e também não escrever nada dentro deles?
'''

import os

frutas = ['maçã', 'banana', 'uva', 'limão', 'morango']
cores = ['verde', 'amarelo', 'azul', 'vermelho', 'rosa']
linguagens_de_programacao = ['python', 'java script', 'java', 'c++', 'kotlin']

# Desafio 1 - Crie um novo arquivo chamado frutas.txt e insira dentro dele todos as 5 frutas que estão na lista de frutas
with open('desafio manipular e salvar/frutas.txt', 'w', newline='', encoding='utf-8') as file:
    for fruta in frutas:
        file.write(fruta + os.linesep)

# Desafio 2 - Imprima na tela todas as linhas que estao dentro do arquivo frutas.txt
with open('desafio manipular e salvar/frutas.txt', 'r', encoding='utf-8') as file:
    for line in file:
        print(line)


# Desafio 3 - Sem apagar os dados que já estão dentro de frutas.txt, adicione todas as cores que estão dentro da sua lista de cores ao arquivos frutas.txt
with open('desafio manipular e salvar/frutas.txt', 'a', newline='', encoding='utf-8') as file:
    for cor in cores:
        file.write(cor + os.linesep)
        
# Desafio 4 - Crie um novo arquivo chamado 'Top 5 Linguagens.txt' e popule o arquivo, de forma com que cada linuguagem ocupe apenas uma linha.
with open('desafio manipular e salvar/top_5_linguagens.txt', 'w', newline='', encoding='utf-8') as file:
    for linguagem in linguagens_de_programacao:
        file.write(linguagem + os.linesep)


# BONUS - Como você poderia criar vários arquivos diferentes usando um laço for e strings dinâmicos(f'{}'), e também não escrever nada dentro deles?

while True:
    nome_do_arquivo = input('Nome do arquivo: ')
    with open(f'desafio manipular e salvar/{nome_do_arquivo}.txt', 'w') as file:
        file.write('')
    
    continuar = input('Deseja continuar? ')
    if continuar not in ('sim', 's'):
        break

# Outra forma de resolver o exercicio bonus
files = ['musica.mp3', 'relatório.pdf', 'foto.png', 'senha.txt']
for file in files:
    with open(f'desafio manipular e salvar/{file}', 'w') as arquivo:
        pass