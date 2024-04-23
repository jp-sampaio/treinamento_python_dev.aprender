import json 

# Criar ou ler JSON existente 
computador_json = """{
    "marca": "dell",
    "preço": 1500
}"""

# Lendo uma string JSON 
data = json.loads(computador_json) # Transforma uma String JSON em um dicionário 
print(data['preço'])

# Salvar um String JSON para Arquivo JSON
with open('computador.json', 'w', encoding='utf-8') as arquivo_json:
    json.dump(computador_json, arquivo_json)

# Para ler um arquivo JSON
with open('computador.json', encoding='utf-8') as arquivo_json:
    string_computador_json = json.load(arquivo_json) # Transforma o JSON para string
    dicionario_computador_json = json.loads(string_computador_json) # Converte de String para dicionário
    print(dicionario_computador_json['marca'])



# Desafio para criar um json somente utiliazando codigo python

pessoa = """{
    "name": "John Smith",
    "age": 30,
    "city": "New York",
    "isStudent": true, 
    "gpa": 3.5
}"""

with open('pessoa.json', 'w', encoding='utf-8') as arquivo_json:
    json.dump(pessoa, arquivo_json)