# Forma pratica de utilizar o logging em um cenario real
import logging

#                        nivel             nome do arquivo      append          informações que vão aparecer na messagem
logging.basicConfig(level=logging.DEBUG, filename='app_2.log', filemode='a', format='%(levelname)s - %(message)s - %(asctime)s')

try:
    email = input('Digite seu e-mail: ')
    senha = int(input('Digite sua senha bancária: '))
    if senha == 1234:
        logging.info(f'{email} entrou em sua conta bancária')
except ValueError as erro:
    print('Favor digitar apenas números')
    logging.warning(erro)