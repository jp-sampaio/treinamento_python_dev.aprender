# O conceito de decorator provê uma maneira simples de modificar o comportamento de uma função sem necessariamente alterá-la. 
# Em outras palavras é uma função que atribui uma nova funcionalidade a uma outra função

from datetime import datetime

def depositar_dinheiro():
    print('Depósitando dinheiro')

    def depositar_dolar():
        print('Depósitando dolar')
    
    def depositar_reais():
        print('Depósitando reais')
    
    depositar_dolar()
    depositar_reais()

depositar_dinheiro()


def pai(numero):
    def filho_1():
        print('Eu sou o filho 1')
    def filho_2():
        print('Eu sou o filho 2')
    if numero == 1:
        return filho_1 # Retornando a referência da função
    
resultado = pai(1)
resultado()


def meu_decorator(funcao):
    def wrapper():
        print('Antes')
        funcao()
        print('Depois')
    
    return wrapper

@meu_decorator
def parabenizar():
    print('Parabéns!!!')

parabenizar()

# @meu_decorator já faz esse passo abaixo e decora a função que pode ser usada normalmente
# imprimir = meu_decorator(parabenizar)
# imprimir()


#=========================== Desafio =================================
# Desafio
# Crie um decorator que irá pegar a função que for passada para ele e imprimir o horário atual antes de executar a função e despois imprimir o horário após
#  ter finalizado a execução da função.

hora = datetime.now()

def horario(funcao):
    def wrapper():
        print(f'{hora.hour}:{hora.minute}:{hora.second}')
        funcao()
        print(f'{hora.hour}:{hora.minute}:{hora.second}')

    
    return wrapper

@horario
def executar():
    print('Executando o programa!!!')

executar()