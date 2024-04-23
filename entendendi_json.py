import json

# Primeiro arquivo json simples
# Foi utilizado o utf 8 porque no json existe caractes especiais
with open('materialdeapoio/arquivos json usuarios/usuarios1.json', encoding='utf-8') as arquivo_json:
    data = json.load(arquivo_json) # Converter arquivo JSON -> String
    print(data['nome'])

# Segundo arquivo JSON com uma lista como propriedade de uma chave
with open('materialdeapoio/arquivos json usuarios/usuarios2.json', encoding='utf-8') as arquivo_json:
    data = json.load(arquivo_json)
    print(data['permissões'][1])
    

# Terceiro arquivo json com apenas uma chave contendo uma lista com dois dicionarios
with open('materialdeapoio/arquivos json usuarios/usuarios3.json', encoding='utf-8') as arquivo_json:
    data = json.load(arquivo_json)
    print(data['usuários'][0]['permissões'][2])
    print(data['usuários'][1]['admin'])


# Quarto arquivo json muito parecido com o terceiro mas dicionarios dentro da lista.
with open('materialdeapoio/arquivos json usuarios/usuarios4.json', encoding='utf-8') as arquivo_json:
    data = json.load(arquivo_json)
    print(data['usuários'][1]['plano']['preco'])
    print(data['usuários'][0]['telefone'])

# Quinto arquivo json começa com uma lista e tem como valores duas coleções de dicionários 
with open('materialdeapoio/arquivos json usuarios/usuarios5.json', encoding='utf-8') as arquivo_json:
    data = json.load(arquivo_json)
    print(data[0]['admin'])
    print(data[1]['plano']['nome'])