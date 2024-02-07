from flask import Flask,render_template, jsonify, request
from algorithms import ceaser_cipher

app = Flask(__name__)

def encryption_function(plaintext,encryption_key,encryption_technique):
    if encryption_technique == 'caesar':
        return ceaser_cipher.encryption_algorithm(plaintext,encryption_key)

# def ceaser_cipher_algorithm():
#     encrypted_text = ceaser_cipher.encryption_algorithm()
#     decrypted_text = ceaser_cipher.decryption_algorithm(encrypted_text)
#     return jsonify({
#         'encrypted_text': encrypted_text,
#         'decrypted_text': decrypted_text
#     })

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
    return

@app.route('/receive_message', methods=['POST'])
def receiver():
    return