"""
    DESAFIO API músicas 🥇
    ### 1. Definir o objetivo da API:
    Iremos montar uma api de músicas, onde deverá ser possível, consultar todas canções disponíveis, consultar uma canção individual, editar canções existentes e também excluir músicas existentes.
    ### 2. Qual será o URL base da API?
    Iremos utilizar o url base 'localhost'
    ### 3. Quais são os endpoints?
    Disponibilize endpoints para consultar, editar, criar e excluir
    ### 4. Quais recursos serão disponibilizados pela API?
    Informações sobre canções
    ### 5. Quais verbos http serão disponibilizados?
    * GET
    * POST
    * PUT
    * DELETE
    ### 6. Quais são os URLs completos para cada um?
    * GET http://localhost:5000/cancoes
    * GET http://localhost:5000/cancoes/1
    * POST http://localhost:5000/cancoes
    * PUT http://localhost:5000/cancoes/1
    * DELETE http://localhost:5000/cancoes/1
    ### 7. Qual deve ser a estrutura de cada canção
    - lista de dicionários, que contem cancao e estilo
"""

from flask import Flask, jsonify, request

app = Flask(__name__)

cancoes = [
    {
        'cancao': 'Coracao Machucado',
        'estilo': 'Forro'
    },
    {
        'cancao': 'Garota de Ipanema',
        'estilo': 'Bossa Nova'
    },
    {
        'cancao': 'Melhor Eu Ir',
        'estilo': 'Pagode'
    },
    {
        'cancao': 'Diante do Rei',
        'estilo': 'Catolica'
    }
]

# GET http://localhost:5000/cancoes
@app.route('/', methods=['GET'])
def obter_cancoes():
    return jsonify(cancoes)

# GET com id http://localhost:5000/cancoes/1
@app.route('/cancoes/<int:indice>', methods=['GET'])
def obter_cancao_especifica(indice):
    return jsonify(cancoes[indice], 200)

# POST http://localhost:5000/cancoes
@app.route('/cancoes', methods=['POST'])
def criar_cancao():
    cancao = request.get_json()
    cancoes.append(cancao)

    return jsonify(cancoes)

# PUT http://localhost:5000/cancoes/1
@app.route('/cancoes/<int:indice>', methods=['PUT'])
def atualizar_cancao(indice):
    cancao = request.get_json()
    cancoes[indice].update(cancao)

    return jsonify(cancoes[indice], 200)

# DELETE http://localhost:5000/cancoes/1
@app.route('/cancoes/<int:indice>', methods=['DELETE'])
def excluir_cancao(indice):
    try:
        if cancoes[indice] is not None:
            del cancoes[indice]
            return jsonify(f'Musica excluida com sucesso {cancoes[indice]}', 200)
    except:
        return jsonify('Não foi possível encontrar a canção na lista', 404)

app.run(port=5000, host='localhost', debug=True)