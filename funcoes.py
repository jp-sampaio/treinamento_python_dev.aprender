# sintases básica de uma função
# def nome_da_funcao(parametros):
#    comando
# nome_da_funcao() caso tenha parâmetros passa nos parânteses

# função sem parâmetros
def dar_boas_vindas():
    print('Seja bem-vindo"')
dar_boas_vindas()

# Função com parâmetros
def seja_bem_vindo(nome):
    print(f'Seja bem-vindo {nome}')
seja_bem_vindo('João Paulo')

# Função com valor padrão no parâmetro
def apresentar_lugar(lugar='nossa loja'):
    print(f'Conheça {lugar}')
apresentar_lugar('Cajueirinho') # Se o parênteses for vazio vai ser o valor padrão, caso seja outro valor vai ser ele que será mostrado

# O valor que é padrão precisar ser o último a ser declarado 
def apresentar_lugar_e_horario(horario_de_funcionamento, lugar='nossa loja'):
    print(f'Conheça {lugar} que esta aberta das {horario_de_funcionamento}')
apresentar_lugar_e_horario('08:00 as 16:00') # Valor conrresponde ao horário de funcionamento


#  ============================= Desafio =========================================

# Desafio🥇

# DESAFIO 1 - Crie uma função chamada gerar_nome_completo que recebe como parâmetro o nome e sobrenome de alguém e dá boas vindas para essa pessoa

def gerar_nome_completo(nome, sobrenome):
    print(f'Seja bem-vindo {nome} {sobrenome}')

gerar_nome_completo('João', 'Sampaio')

# DESAFIO 2 - # Crie uma função chamada calcular_valores que recebe 2 parâmetros o primeiro o preco de um produto e o segundo parâmetro é a quantidade, 
# porém a quantidade deve haver um valor padrão de 1. Sua função deve exibir o resultado do preço do produto, multiplicado a quantidade escolhida.

def calcular_valores(preco, quantidade=1):
    resultado = preco * quantidade
    print(resultado)

calcular_valores(20, 2)