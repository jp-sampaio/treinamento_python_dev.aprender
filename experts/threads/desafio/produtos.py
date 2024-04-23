# Rodar 5 threads simutâneamente

import threading
import time

products = ['Celular', 'Monitor', 'Fone de Ouvido', 'Alto Falante', 'Computador']

threads = []

def navegar_site(site, product):
    print(f'Navegando até o site: {site} e pesquisando sobre o {product}')
    time.sleep(5)
    print(f'{product} processado com sucesso')

for i in range(5):
    new_thread = threading.Thread(target=navegar_site, args=('https://mercadolivre.com.br', products[i]), daemon=True)
    threads.append(new_thread)

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()