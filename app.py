from flask import Flask, request, jsonify
from mailer import Mailer

app = Flask(__name__)

@app.route('/index')
def index():
    return '<h1>What a Beautiful Day!</h1>'


@app.route('/get', methods=['POST'])
def mail():
    data = request.get_json()
    return jsonify({'My_Result': data})


@app.route('/webhook', methods=['POST'])
def mail():
    data = request.get_json()
    data = data['queryResult']['parameters']
    details = {'name':data['customer_name'], 'email':data['customer_email'], 'phone':data['customer_phone'], 'service_type':'Service '+str(data['number'])}
    receiver = 'adityakiran.cs@gmail.com'
    emailer = Mailer(receiver,details)
    emailer.mail()

    return jsonify({'My_Result': details})


@app.route('/author', methods=['GET'])
def name():
    return '<h3>Created by Aditya Kiran Pal, adityakiran.cs@gmail.com</h3>' 

