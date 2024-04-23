import random
from pprint import pprint

# Desafio 1

'''
    Crie a seguir, selecionando o ganhador aleatóriamente um nomes da lista de participantes. A ideia é simular quem irá ganhar cada sorteio, sua lista deve gerar a seguinte estrutura(porém o nome pode vir a ser diferente, já que estamos selecionando os nomes aleatóriamente):
    {
        "sorteio1": 'cris',
        "sorteio2": 'rafael',
        "sorteio3": 'marcus',
    }
'''
#  Usando a lista seguir como base:
sweepstakes = ['sorteio1','sorteio2','sorteio3']
participants = ['joel','jessica', 'maria','cris','Larissa', 'rafael', 'marcus', 'john']

winners = {prize_draw: random.choice(participants) for prize_draw in sweepstakes}

pprint(winners)

# ===========================================================================================================================

# Desafio 2 

'''
    Precisamos de dados de testes para criar contas temporárias, no momento precisamos gerar 5 valores de 1 à 100, e esses valores precisam ser gerados 5 valores de 1 a 100 aleatóriamente. E estes valores precisam ser gerados para cada grupo na lista abaixo:

    grupos = ['grupo 1', 'grupo 2', 'grupo 3']
    
    O resultado esperado é o dicionário com a estrutura a seguir(os valores entre contindos dentro da lista estarão diferentes, uma vez que os valores abaixo foram geradores aleatóriamente)
    {

    'grupo 1': [93, 97, 63, 36, 34],

    'grupo 2': [81, 24, 22, 46, 52],

    'grupo 3': [5, 35, 6, 86, 37]

    }
'''

groups = ['grupo 1', 'grupo 2', 'grupo 3']

random_values_in_groups = {group: [random.randint(1, 101) for i in range(5)] for group in groups}

pprint(random_values_in_groups)