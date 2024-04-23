# Temos basicamente dos frameworks para desenvolver api no python: Flask e o Django
from flask import Flask, jsonify, request

# Instânciando o flask com o nome padrão do arquivo que ele está presente
app = Flask(__name__)

"""
    1- Definir o objetivo do API:
    ex: Iremos montar uma api de blog, onde eu poderia consultar, editar, criar ou excluir postagens em um blog usando a api.

    2- Qual será a URL base do api?
    ex: Quando você criar uma aplicação local ela terá uma url do tipo http://localhost:5000, porém quando você for subir isso para a nuvem, você terá que comprar ou usar um domínio como url base, vamos imaginar um exemplo de "devaprender.com/api/"

    3- Quais sãp os endpoints?
    ex: Se seu requisito é de poder consultar, editar, criar e excluir, você terá que disponibilizar os endpoints para essas postagens: /postagens

    4- Quais recursos serão disponibilizados pela api?
    Informações sobre as postagens

    5- Quais os verbs http serão disponibilizados?
    * GET
    * POST
    * PUT
    * DELETE

    6- Quais são as url completas para cada um?
    * GET http://localhost:5000/postagens
    * GET id http://localhost:5000/postagens/1
    * POST http://localhost:5000/postagens
    * PUT id http://localhost:5000/postagens/1
    * DELETE id http://localhost:5000/postagens/1
"""

# Simulando uma postagem vindo de uma banco de dados 
postagens = [
    {
        'título': 'Minha Historia',
        'autor': 'Amanda Dias'
    },
    {
        'título': 'Novo Dispositivo Sony',
        'autor': 'Howard Stringer'
    },
    {
        'título': 'Lançamento do Ano',
        'autor': 'Jeff Bezos'
    }
]

# Com o decorator criar uma rota padrão - GET http://localhost:5000
@app.route('/')
def obter_postagens():
    return jsonify(postagens)

# Obter uma nova postagem com id - GET id http://localhost:5000/postagem/1
@app.route('/postagem/<int:indice>', methods=['GET'])
def obter_postagens_por_indice(indice):
    return jsonify(postagens[indice]) # É utilizado o indice porque o nosso json é uma lista 

# Criar uma nova postagem - POST http://localhost:5000/postagem
@app.route('/postagem', methods=['POST'])
def criar_nova_postagem():
    postagem = request.get_json()
    postagens.append(postagem)

    return jsonify(postagem, 200)

# Alterar postagem existente - PUT http://localhost:5000/postagem/0
@app.route('/postagem/<int:indice>', methods=['PUT'])
def alterar_postagem(indice):
    postagem_alterada = request.get_json()
    postagens[indice].update(postagem_alterada)

    return jsonify(postagens[indice], 200)


# Excluir uma postagem - DELETE http://localhost:5000/postagem/0
@app.route('/postagem/<int:indice>', methods=['DELETE'])
def excluir_postagem(indice):
    try:
        if postagens[indice] is not None:
            del postagens[indice]
            return jsonify(f'Foi excluído a postagem {postagens[indice]}', 200)
    except:
        return jsonify('Não foi possível encontrar a postagem para a exclusão', 404)
    
app.run(port=5000, host='localhost', debug=True)