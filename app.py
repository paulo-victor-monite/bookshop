from flask import Flask, jsonify, request

app = Flask(__name__)

livros = [
    {
        'id': 1,
        'titulo': 'Clube da Luta',
        'autor': 'Chuck Palahniuk'
    },
    {
        'id': 2,
        'titulo': '1984',
        'autor': 'George Orwell'
    },
    {
        'id': 3,
        'titulo': 'Dom Quixote',
        'autor': 'Miguel de Cervantes'
    }
]

# Consultador todos


@app.route('/livros', methods=['GET'])
def getAll():
    return jsonify(livros)

# Constultar por ID


@app.route('/livros/<int:id>')
def getById(id):
    for livro in livros:
        if livro.get('id') == id:
            return jsonify(livro)


app.run(port=4500, host='localhost', debug=True)
