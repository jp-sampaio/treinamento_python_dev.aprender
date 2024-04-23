# Datetime e time servem para pegar a data e hora atual além de poder definir de forma manuel e dinâmica.

# Importar o datetime do módulo datetime
from datetime import datetime

# print(datetime.now()) # Data e hora atual
# print(datetime.now().day) # Dia atual
# print(datetime.now().month) # Mês atual
# print(datetime.now().year) # Ano atual
# print(datetime.now().hour) # Hora atual

# # Criar uma data
# lancamento_app = datetime(2021, 5, 25, 12, 20, 56)
# print(lancamento_app)

# # Quero receber a data de lançamento do meu aplicativo 
# # 25/08/2024

# # Tenho que converter o tipo de data recebido pelo input, já que vem em string e o valor suportado pelo datetime é do tipo int
# data_de_lancamento = datetime.strptime(input('Quando devemos o aplicativo? '), '%d/%m/%Y') # Formato de data americano
# print(data_de_lancamento)
# print(type(data_de_lancamento))

# # Prazo até a data de lançamento do meu app
# data_atual = datetime.now()
# prazo = data_de_lancamento - data_atual
# print(prazo)

#  Desafio => quantos dias faltam até o meu aniversário.
# Datetime já foi importada no inicio do programa

current_date = datetime.now()
print(current_date)
birthday = datetime.strptime(input('Digite a data do seu aniversário: '), '%d/%m/%Y')
# Outra forma de pegar a data de aniversário
# birthday = datetime(2024, 7, 11)

days_for_my_birthday = birthday - current_date

print(days_for_my_birthday)