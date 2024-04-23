import json

with open('desafio.json', encoding='utf-8') as arquivo_json:
    # Imprimir o e-mail do usuário com id 2
    data = json.load(arquivo_json)
    print(data['user'][1]['email'])
    # imprimir a city do usuário com id 1
    print(data['user'][0]['address']['city'])
    # Imprimir o total do pedido do usuário com id 2
    print(data['user'][1]['orders'][0]['total'])    