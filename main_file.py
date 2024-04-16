from flask import Flask,render_template, jsonify, request
from algorithms import ceaser_cipher
from algorithms import hill_cipher
from algorithms import monoalphabetic
from algorithms import playflair
from algorithms import deffie_heilman
from algorithms import Columnar
from algorithms import DES
from algorithms import otp
from algorithms import RailFence
from algorithms import aes
from algorithms import polyalphabetic
from algorithms import ECC
from algorithms import rc4
from algorithms import rsa

app = Flask(__name__)

def encryption_function(plaintext,encryption_key,encryption_technique):
    if encryption_technique == 'caesar':
        return ceaser_cipher.encryption_algorithm(plaintext,encryption_key)
    if encryption_technique == 'hill_cipher':
        return hill_cipher.encryption_algorithm(plaintext,encryption_key)
    if encryption_technique == 'monoalphabetic':
        return monoalphabetic.encryption_algorithm(plaintext)
    if encryption_technique == 'play_flair':
        return playflair.encryption_algorithm(plaintext,encryption_key)
    if encryption_technique == 'polyalphabetic':
        return polyalphabetic.encryption_algorithm(plaintext,encryption_key)
    if encryption_technique == 'railfence':
        return RailFence.encryption_algorithm(plaintext,encryption_key)
    if encryption_technique == 'otp':
        return otp.encryption_algorithm(plaintext,encryption_key)
    if encryption_technique == 'columnar':
        return Columnar.encryption_algorithm(plaintext,encryption_key)
    if encryption_technique == 'aes':
        return aes.encryption_algorithm(plaintext,encryption_key)
    if encryption_technique == 'des':
        return DES.encryption_algorithm(plaintext,encryption_key)
    if encryption_technique == 'deffie':
        return deffie_heilman.encryption_algorithm(plaintext,encryption_key)
    if encryption_technique == 'ecc':
        return ECC.encryption_algorithm(plaintext,encryption_key)
    if encryption_technique == 'rc4':
        return rc4.encryption_algorithm(plaintext,encryption_key)
    if encryption_technique == 'rsa':
        return rsa.encryption_algorithm(plaintext,encryption_key)

def decryption_function(cipher_text,decryption_key,decryption_technique):
    if decryption_technique == 'caesar':
        return ceaser_cipher.decryption_algorithm(cipher_text,decryption_key)
    if decryption_technique == 'hill_cipher':
        return hill_cipher.decryption_algorithm(cipher_text,decryption_key)
    if decryption_technique == 'monoalphabetic':
        return monoalphabetic.decryption_algorithm(cipher_text)
    if decryption_technique == 'play_flair':
        return playflair.decryption_algorithm(cipher_text,decryption_key)
    if decryption_technique == 'polyalphabetic':
        return polyalphabetic.decryption_algorithm(cipher_text,decryption_key)
    if decryption_technique == 'railfence':
        return RailFence.decryption_algorithm(cipher_text,decryption_key)
    if decryption_technique == 'otp':
        return otp.decryption_algorithm(cipher_text,decryption_key)
    if decryption_technique == 'columnar':
        return Columnar.decryption_algorithm(cipher_text,decryption_key)
    if decryption_technique == 'aes':
        return aes.decryption_algorithm(cipher_text,decryption_key)
    if decryption_technique == 'des':
        return DES.decryption_algorithm(cipher_text,decryption_key)
    if decryption_technique == 'deffie':
        return deffie_heilman.decryption_algorithm(cipher_text,decryption_key)
    if decryption_technique == 'ecc':
        return ECC.decryption_algorithm(cipher_text,decryption_key)
    if decryption_technique == 'rc4':
        return rc4.decryption_algorithm(cipher_text,decryption_key)
    if decryption_technique == 'rsa':
        return rsa.decryption_algorithm(cipher_text,decryption_key)

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
    