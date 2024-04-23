# Criando um site que vai rodar duas tarefas diferentes com o auxilio do threads

import webbrowser # Esse módulo vai buscar um site que vou passar como argumento;
import threading # Com esse módulo eu posso rodar tarefas simultâneas;
import time # Módulo para definir um delay e simular um servidor na web;

# Função que vai abrir o site e fazer uma contagem de 1 à 19 
def extrair_dados_do_site(site):
    print(f'Estamos navegando até o site {site}')
    webbrowser.open_new(site) # Essa linha vai abrir o site.
    for i in range(1, 20):
        print(f'Processando os dados - {i}/19')
        time.sleep(1)
    print('Finalizando a extração de dados do site')


# Função que vai contar de 1 à 10 
def baixar_arquivos():
    for i in range(1, 11):
        print(f'Baixando arquivos - {i}/10')
        time.sleep(1)
    print('Arquivos baixados')

# Cria uma nova thread que vai executar a função extrair dados do site 
nova_thread = threading.Thread(
    # É necessário uma vírgula a mais nos args porque ela é uma tupla
    target=extrair_dados_do_site, args=('https://devaprender.com',), daemon=True
)

# Executar a nova thread e vai executar o que tiver logo em seguida
nova_thread.start()
baixar_arquivos() # Essa função é executada simutâneamente com a do thread
nova_thread.join() # Isso permite encerrar a thread, caso ela tivesse sido declarada antes da função baixar arquivos a thread tinha encerrado e não havia sido executado em paralelo 