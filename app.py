from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>What a Beautiful Day!</h1>'


@app.route('/webhook', methods=['POST'])
def mail():
    data = request.get_json()
    return jsonify({'result': data})


@app.route('/try', methods=['GET'])
def name():
    return 'Aditya Kiran Pal' 

