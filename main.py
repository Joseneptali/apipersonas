from flask import Flask, jsonify 
app = Flask(__name__)

@app.route('/personas', methods=['GET'])
def index():
    lista_personas=[
        {'name':'Jose Rosania Vargas'},
        {'name':'TONY STARK'},
        {'name':'ELON MUSK'},
        {'name':'JIM CAVIEZEL'},
        {'name':'HALO'},
        {'name':'PEDRO PICAPIEDRA'},
        {'name':'ROBERTO GOMEZ BOLAÑOS'}

    ]
    return jsonify(lista_personas)
if __name__ == '__main__':
    app.run(debug=True)