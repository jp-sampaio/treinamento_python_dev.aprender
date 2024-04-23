# Porque comparar?
# No nosso dia a dia, precisamos comparar dados para saber se eles 
# são iguais, diferentes, maior, menor, maior e igual ou menor e igual.

# O operador de Igualdade ==.
# O operador de Diferença !=.
# O operador de Maior >.
# O operador de Menor <.
# O operador de Maior e igual >=.
# O operador de Menor e igual <=.

# Ele retorna True se a comparação for verdadeira e False se a comparação for falsa.
# Exemplo: maior de idade

age = int(input('Digite a sua idade '))
majority = 18
# igualdade
print(age == majority) 
# diferente
print(age != majority)
# maior
print(age > majority)
# menor
print(age < majority)
# maior e igual
print(age >= majority)
# menor e igual
print(age <= majority)


# Além de números o python tambem compara outros tipos de dados.
# Exemplo:
# Comparando strings, o python também diferencia o maiúsculo do minúsculo
name = 'João'
print(name == 'João')
print(name != 'João')
print(name > 'João')
print('b' > 'a')

# Comparando booleanos
# True = 1
# False = 0
# Esse aqui apontam para a memória 
print(True is True)
print(True is not False)

# Comparando número com string
# O python não consegue comparar um número com uma string
print(1 == '1')
print(1 != '1')
