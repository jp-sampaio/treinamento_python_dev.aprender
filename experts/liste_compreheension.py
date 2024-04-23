# A list compreheesion serve para executar um loop ou condicional e retorna uma lista com o resultado 

# Lista com os números pares de uma lista
# Posso criar uma lista ou utilizar o range
from pprint import pprint

numeros_dobrados = [numero * 2 for numero in range(1, 6)]
# pprint(numeros_dobrados) # [2, 4, 6, 8, 10]


# Utilizando uma função na expressão 
def aprovados(aluno):
    return aluno + ' Aprovado'

alunos = ['Bruno', 'Carlos', 'Monica', 'Ana', 'Joana', 'Pablo']

situacao_aluno = [aprovados(aluno) for aluno in alunos]
# pprint(situacao_aluno)


# Fazer uma matriz utilizando um for na expressão sem a necessidade de criar listas
'''
    resultado final deve ficar assim
    1, 2, 3, 4, 5
    1, 2, 3, 4, 5
    1, 2, 3, 4, 5
    1, 2, 3, 4, 5
    1, 2, 3, 4, 5
'''

matriz = [[i for i in range(1, 6)] for x in range(5)]
# pprint(matriz)

# É a mesma coisa que eu utilizar da forma mais comprida
matriz_comprida = []
for linha in range(5):
    linha_matriz = []
    for coluna in range(1, 6):
        linha_matriz.append(coluna)
    
    matriz_comprida.append(linha_matriz)

# print(matriz_comprida)

# for linha in matriz_comprida:
    # print(linha)

# Usar condicionais na list compreheesion 
# Sintaxes [expressão for membro in iteravel (condicional if)]
nomes = ['maria', 'marcia', 'joão', 'lucas', 'pamela']
# A função aprovado já foi declarada acima 
aprovado_ou_nao = [aprovados(nome) for nome in nomes if nome != 'lucas']
# pprint(aprovado_ou_nao)

# Valores númericos 
show_number = [numero for numero in range(1, 21) if numero not in (3, 6, 12, 14)] # Exceto esses números
# print(show_number)

# Mostrar somente os números pares 
def pair_number(number):
    if number % 2 == 0:
        return True
    else:
        return False

show_even_number = [number for number in range(20) if pair_number(number)]
# print(show_even_number)


# As condicionais são flexiveis e podem ser declaradas tanto no inicio como no final
participants = ['mario', 'monica', 'paloma', 'vinicios', 'maria', 'antonio']
winners = ['paloma', 'antonio']

# Passa por todos os nomes em participantes e caso eles estejam também em ganhadores mostra a mensagem ganhador junto com o nome, senão mostra a mensagem perdedor juntamente com o nome.
show_winners = [nome + ' Ganhador(a)' if nome in winners else nome + ' Perdedor(a)' for nome in participants]
print(show_winners)