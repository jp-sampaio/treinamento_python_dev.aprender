import math

# Tipos de números que podem ser usados em python
# int => 4
# float => 4.5

# Tipos de operações que podem ser usados e exemplos de operações em python:
# + => print(2 + 2) soma
# - => print(2 - 2) subtração
# * => print(2 * 2) multiplicação
# / => print(2 / 2) divisão
# ** => print(2 ** 2) potenciação
# // => print(2 // 2) divisão inteira
# % => print(2 % 2) resto da divisão

print(2 + 2) # 4
print(2 - 2) # 0
print(2 * 2) # 4
print(2 / 2) # 1
print(2 ** 2) # 4
print(2 // 2) # 1
print(2 % 2) # 0

# Exemplo de operações com strings:
# print('2' + '2') => Concatena as duas strings 
# print('2' - '2') => Não é possível fazer operações com strings
# print('2' * '2') => Não é possível fazer operações com strings
# print('2' / '2') => Não é possível fazer operações com strings
# print('2' ** '2') => Não é possível fazer operações com strings
# print('2' // '2') => Não é possível fazer operações com strings
# print('2' % '2') => Não é possível fazer operações com strings

# Exemplo de atribuição mais rápida 
a = 2
# Forma rápida de fazer a atribuição mais rápida e serve para todas as operações
# a = a + 2 é o mesmo que a += 2
a += 2
print(a)

# Exemplo de atribuição com multiplas variáveis
a, b, c = 2, 3, 4
# Exemplo de atribuição com multiplas variáveis e valores padrão
a = b = c = 2

# Operações matemáticas
# Arredonda para o valor mais próximo
print(round(2.6))

# A biblioteca Math possui funções matemáticas
# Math foi importada no início do arquivo

# Função para calcular a raiz quadrada
print(math.sqrt(4))
# Função para calcular o fatorial
print(math.factorial(4))
# Função para mostrar o valor de pi
print(math.pi)
# Função para arredondar para cima
print(math.ceil(2.2))