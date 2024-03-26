from flask import Flask,render_template, jsonify, request
from algorithms import ceaser_cipher
from algorithms import hill_cipher

app = Flask(__name__)

def encryption_function(plaintext,encryption_key,encryption_technique):
    if encryption_technique == 'caesar':
        return ceaser_cipher.encryption_algorithm(plaintext,encryption_key)
    if encryption_technique == 'hill_cipher':
        return hill_cipher.encryption_algorithm(plaintext,encryption_key)

def decryption_function(cipher_text,decryption_key,decryption_technique):
    if decryption_technique == 'caesar':
        return ceaser_cipher.decryption_algorithm(cipher_text,decryption_key)
    if decryption_technique == 'hill_cipher':
        return hill_cipher.decryption_algorithm(cipher_text,decryption_key)

@app.route('/')
def render_design_template():
    return render_template('design_template.html')

@app.route('/encrypt', methods=['POST'])
def encrypt():
        plaintext = request.form['plain_text']
        encryption_key = request.form['key']
        encryption_technique = request.form['algorithm']
        encrypted_text = encryption_function(plaintext,encryption_key,encryption_technique)
        return render_template('design_template.html',encrypted_text = encrypted_text)

@app.route('/send_message', methods=['POST'])
def sender():
    send_encrypted_text = request.form['encrypted_text']
    return render_template('design_template.html',send_encrypted_text = send_encrypted_text)

@app.route('/receive_message', methods=['POST'])
def receiver():
    cipher_text = request.form['received_encrypted_text']
    decryption_key = request.form['key']
    decryption_technique = request.form['algorithm']
    plain_text = decryption_function(cipher_text,decryption_key,decryption_technique)
    return render_template('design_template.html',decrypted_text = plain_text)
    