# Como utilizar os 4 principais comandos (verbos) de uma API

import requests
from pprint import pprint

url = 'https://jsonplaceholder.typicode.com/todos'
id_do_recurso = 2

# GET - Obter os dados de todos os recursos
resultado_get = requests.get(url)
# pprint(resultado_get.json())

# GET com ID - Obter os dados de um recurso especifico
resultado_get_com_id = requests.get(f'{url}/{id_do_recurso}')
# pprint(resultado_get_com_id.json())

# POST - Criar um novo recurso 
# Criar o novo recurso que vai ser adicionado no recurso anterior, não foi adicionado o id porque vai ser criado dinamicamente
nova_tarefa = {
    'completed': False,
    'title': 'Lavar o carro',
    'userId': 1
}

resultado_post = requests.post(url, nova_tarefa) # A url e a nova tarefa como parâmetros
# pprint(resultado_post.json())

# PUT - Alterar ou atualizar um recurso já existente
# Criar a nova tarefa que irá atualizar a antiga
tarefa_atualizada = {
    'completed': False,
    'title': 'Lavar a moto',
    'userId': 1
}

resultado_put = requests.put(f'{url}/{id_do_recurso}', tarefa_atualizada)
# pprint(resultado_put.json())

# DELETE - Excluir um recurso já existente
resultado_delete = requests.delete(f'{url}/{id_do_recurso}')
pprint(resultado_delete.json())