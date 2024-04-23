# Utilizando o try e except para tratar erros
# try:
#     valor = int(input('Digite um valor em dolares: '))
#     print(valor * 5.25)
# except:
#     print('Favor digitar somente números!')


# Especificando o tipo de erro
# try:
#     meses = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
#     print(meses[15])
# except IndexError as erro:
#     print('Favor digitar um índice válido')
#     print(erro) # Mostra o erro, mas não mostrar para o usuario


# Utilizando o finally e vários except de tratamento
try:
    value = int(input('Digite um valor: '))
    print(value / 0)
except ZeroDivisionError as erro:
    print('Não é possível dividir por zero!')
except ValueError as erro:
    print('Favor digitar somente números')
finally:
    # Aqui vai o código que será executado independente das exceção 
    print('A operação foi cancelada!')