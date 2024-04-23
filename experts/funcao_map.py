# O metodo map é utilizado para executar uma função em cada item de uma lista 

# Forma simples de criar uma função com o range
lista_comun = []
for i in range(5):
    lista_comun.append(i)
# print(lista_comun)

# Criando lista com a utilização do map
nomes = ['Manoel', 'Marcos', 'Vitoria', 'Joaquim', 'Melissa', 'Elen']

def aprovar_aluno(nome):
    return nome + ' APROVADO'

# Printando o resultado da lista do map que passa a função e o interavel
# print(list(map(aprovar_aluno, nomes)))

# Aprimorando o exemplo acima
alunos = [
    {
        'nome': 'Manoel',
        'nota': 7.0
    },
    {
        'nome': 'Marcos',
        'nota': 8.0
    },
    {
        'nome': 'Vitoria',
        'nota': 6.0
    },
    {
        'nome': 'Joaquim',
        'nota': 8.7
    },
    {
        'nome': 'Melissa',
        'nota': 7.0
    },
    {
        'nome': 'Elen',
        'nota': 5.6
    },
]
def aprovando_aluno(aluno):
    if aluno['nota'] >= 7.0:
        return f'O aluno {aluno['nome']} foi aprovado com nota {aluno['nota']}.'
    else:
        return f'O aluno {aluno["nome"]} foi reprovado com nota {aluno["nota"]}.'
    
    
aprovacao_ou_reprovacao = list(map(aprovando_aluno, alunos))

for i in range(len(aprovacao_ou_reprovacao)):
    print(aprovacao_ou_reprovacao[i])