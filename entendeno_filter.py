# Filter
# A função filter permite aplicar uma função de filtro por uma coleção e retorna somente a condição verdadeira 

nomes = ['Larissa', 'Rafael', 'Marcus', 'John']

def aprovar_pessoa(pessoa):
    if pessoa == 'Marcus':
        return True
    else:
        return False

print(list(filter(aprovar_pessoa, nomes))) # Retorna somente a condição verdadeira
print(list(map(aprovar_pessoa, nomes))) # Retorna todos os resultados dos itens


pinturas = [
    ['Pinturas Classicas', 'Azul', 1857],
    ['Pintura Medieval', 'Vermelha', 1867],
    ['Pintura Moderna', 'Verde', 1897]
]

def eh_antiguidade(pintura):
    if pintura[2] < 1890:
        return True
    else:
        return False
    
print(list(filter(eh_antiguidade, pinturas)))
print(list(map(eh_antiguidade, pinturas)))


# Desafio 

# DESAFIO 1 🥇

'''
    Usando a lista abaixo, filtre apenas as vagas com salário acima de R$2500,00.
'''

vagas = [
    ['vaga 1', 1200],
    ['vaga 2', 2550],
    ['vaga 3', 5000]
] 

def acima_de_2500(vaga):
    if vaga[1] > 2500:
        return True
    else:
        return False

print(list(filter(acima_de_2500, vagas)))