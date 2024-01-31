from flask import Flask,render_template, jsonify
from algorithms import ceaser_cipher

app = Flask(__name__)

@app.route('/')
# def render_design_template():
#     return render_template('design_template.html')

@app.route('/')
def ceaser_cipher_algorithm():
    encrypted_text = ceaser_cipher.encryption_algorithm()
    decrypted_text = ceaser_cipher.decryption_algorithm(encrypted_text)
    return jsonify({
        'encrypted_text': encrypted_text,
        'decrypted_text': decrypted_text
    })