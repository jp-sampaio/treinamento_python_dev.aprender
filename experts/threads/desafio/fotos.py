# Um programa que vai abrir um site e baixar fotos simutâneamente 

import threading
import time

def abrindo_o_site(site):
    print(f'Estamos baixando as fotos do site {site}')

def baixar_fotos(site):
    print(f'Estamos navegando até o site {site}')

nova_thread = threading.Thread(target=baixar_fotos, args=('https://fotos-baixar.com',), daemon=True)

nova_thread.start()
abrindo_o_site('https://fotos.com')
nova_thread.join()