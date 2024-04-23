# Logging é uma forma de mostrar e guadar os erros que podem vir acontecer na aplicação

import logging 

"""
    1 - debug -> Só estou informando informações para os desenvolvedores;
    2 - info -> Só quero informar algo que está acontecendo no meu programa, mas que não é um erro; 
    3 - warning -> Quero alertar sobre algo que está acontecendo, possívelmente fora do esperado, porém ainda não é um erro, mas pode gerar um futuramente;
    4 - error -> Um erro ocorreu na aplicação;
    5 - critical -> Um erro com consequências graves acaba de acorrer na aplicação.
"""

# Armazenar as informações de erros e setar qual será o nivel mais baixo que devera ser mostrado no logging
logging.basicConfig(level=logging.DEBUG, filename='app.log', filemode='w', format='%(levelname)s - %(message)s')
logging.debug('Logging no nivel debug')
logging.info('Logging no nivel info')
logging.warning('Logging no nivel warning')
logging.error('Logging no nivel error')
logging.critical('Logging no nivel critical')