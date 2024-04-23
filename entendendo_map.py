# Podemos criar listas de diferentes formas no python
#  Criar listas usando Loops e Range
numeros = []
for indice in range(5):
    numeros.append(indice)
print(numeros)

# Map
# O Map execuita uma função para cada item de um iteravel seja lista, dicionário ou tupla

nomes = ['Larissa', 'Rafael', 'Marcus', 'John']

def aprovar_pessoa(nome):
    return nome + ' APROVADO'

print(list(map(aprovar_pessoa, nomes)))


# ​DESAFIO -

# Extraia as cores da lista a seguir e coloque as em uma nova lista. Finalmente imprima a nova lista na tela.

pinturas = [

    ['Pintura Classica', 'Azul', 1857],

    ['Pintura Medieval', 'Vermelha', 1867],

    ['Pintura Moderna', 'Verde', 1897]
]

def extrair_cores(cor):
    return cor[1]

lista_de_cores = list(map(extrair_cores, pinturas))
print(lista_de_cores)

cores = []
for pintura in pinturas:
    cores.append(pintura[1])
print(cores)