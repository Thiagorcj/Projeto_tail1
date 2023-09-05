# API  -  é um lugar para disponibilizar recursos ou funcionalidades
# 1 Objetivo - Criar uma API que disponibiliza a consulta, criação, edição e exclusão de livros.
# URL base - localhost
# Endpoints - funcionalidades dentro do API
# localhost/livros (GET)
# localhost/livros/id (POST)
# localhost/livros/id (PUT)
# localhost/livro/id (DELETE)
# Quais recursos - Livros

# Criando API com flask -> pip install flask
from flask import Flask , jsonify, request
# jsonify transforma no formato json(formato esperado dentro de uma API)
app = Flask(__name__)
livros = [
    {
        'id': 1,
        'titulo': 'ABC',
        'autor': 'A'
    },
    {
        'id':2,
        'titulo':'DEF',
        'autor':'B'
    }
]

#Consultar(todos)
@app.route('/livros',methods=['GET'])#Endpoint
def obter_livros():
    return jsonify(livros)
#Consultar(ID)
@app.route('/livros/<int:id>')
def obter_livro_por_id(id):
    for livro in livros:
        if livro.get('id') == id:
            return jsonify(livro)
#Editar
@app.route('/livros/<int:id>',methods=['PUT'])
def editar_livro_por_id(id):
    livro_alterado = request.get_json()
    for indice,livro in enumerate(livros):
        if livro.get('id') == id:
            livros[indice].update(livro_alterado)
            return jsonify(livros[indice])
   
#Criar
@app.route('/livros',methods=['POST'])
def add_livro():
    novo_livro = request.get_json()
    livros.append(novo_livro)
    return jsonify(livros)
#Remover
@app.route('/livros/<int:id>',methods=['DELETE'])
def excluir_livros(id):
    for indice,livro in enumerate(livros):
        if livro.get('id')==id:
            del livros[indice]
    return jsonify(livros)

app.run(port=5000,host='localhost',debug=True)
