# Para que eu consiga processar dados em massa ou operações em massa eu posso utilizar os threadings

import threading
import time
import random

def comentar(site, comentario):
    print(f'Entrando no site: {site}')
    print(f'Deixando um comentário {comentario}')
    time.sleep(5)
    print(f'Dados processados do site: {site}')

comentarios = ['Olá', 'Como vai?', 'Diga', 'Oi', 'Hello', 'Bye']

threads = []
for site in range(10):
    nova_thread = threading.Thread(target=comentar, args=(site, random.choice(comentarios)))
    threads.append(nova_thread)

# Caso fosse necessário que as threads finalize em ordem sequêncial, basta adicionar o join depois do start
for thread in threads:
    thread.start()
    print(f'Iniciando {thread.name}')

for thread in threads:
    thread.join()
    print(f'Finalizando {thread.name}')