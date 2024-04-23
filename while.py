# Número de tentivas para executar determinada ação
# attempts = 0
# while attempts < 3:
#     print('Tente novamente')
#     attempts += 1
# print('Programa finalizado')

# Digite a senha correta 
# password = ''
# while password != '123':
#     password = input('Digite a senha coreta: ')
# print('Seja bem-vindo')

# Não deixe o nome vazio
# name = ''
# while name == '':
#     name = input('Digite o seu nome: ')
# print(f'Bem-vindo {name}')

#  Horário do por do sol
# horario = 0
# while horario <= 17:
#     print(f'Ainda são {horario} hora(s), faltam exatamente {17 - horario} para o por do sol')
#     horario += 1
# print('Hora de ir para o por do sol')

# Decremento com o exemplo do cronometro
# cronometro = 60
# while cronometro >= 0:
#     print(f'{cronometro} minuto(s)')
#     cronometro -= 1
# print('Finalizado')  


# =========================== Desafios ======================================

# DESAFIOS🥇
# DESAFIO 1 - Crie um loop while que irá contar e imprimir no console de 1 até 120
# DESAFIO 2 - Crie um loop while que irá continuamente pedir ao usuário a senha para entrada, e só irá permitir o programa continuar caso ele digite a senha 'secreto'
# DESAFIO 3 - Crie um loop que conte e imprima na tela o valor em ordem descrescente de 100 para 1

contador = 1
while contador <= 120:
    print(contador)
    contador += 1


password = ''
while password != 'secreto':
    password = input('Digite a senha correta: ')
print('Seja bem-vindo!')


number = 100
while number > 0:
    print(number)
    number -= 1
print('Finalizado!')