#  Quando eu quero somente processar uma infrmação em determinado ponto e não desejo utilizar ele mais, eu só processo
# print('Olá')

# Quando vou utilizar essa informação em mais de um ponto e preciso desse dado eu retorno 
# cidade = input('Qual é a sua cidade? ')

def exibir_cotacao_do_dia(moeda):
    if moeda == 'usd':
        print(5.47)

def obter_cotacao_do_dia(moeda):
    if moeda == 'usd':
        return 5.47
    
exibir_cotacao_do_dia('usd')

cotacao = obter_cotacao_do_dia('usd')
if cotacao > 5:
    print('Investir nas ações americanas')
else:
    print('Cotaçaõ não favorável')