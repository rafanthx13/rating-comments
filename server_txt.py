from flask import Flask, request, jsonify, render_template
from flask_cors import CORS, cross_origin
from json import dumps

# Ler modulo proprio
import os, sys
dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, dir_path + '/src')
import textminig_code

# Lidar com Chamada Assincrona
app = Flask(__name__, static_url_path='')
CORS(app)

@app.route("/")
def root():
    return render_template("index.html")

@app.route('/indexx.html')
def roott():
    return render_template('index.html')

@app.route('/get')
@cross_origin
def hello():
    return 'Hello, World!'

@app.route('/rating', methods = ['POST'])
@cross_origin()
def call_test():
	comentario = request.json['comentario']
	return jsonify(textminig_code.classifica(comentario))
	
if __name__ == '__main__':
	port = int(os.environ.get("PORT", 5000))
	app.run(host='0.0.0.0', port=port)

# flask
# flask_cors
# torch
# pandas
