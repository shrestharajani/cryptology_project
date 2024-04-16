
import math
import random

# Generate RSA keys
def generate_keys(p, q):
    n = p * q
    phi = (p - 1) * (q - 1)
    e = 65537  # Common public exponent
    d = pow(e, -1, phi)  # Private exponent
    return (e, n), (d, n)

# RSA Encryption
def encryption_algorithm(message, public_key):
    e, n = public_key
    ciphertext = [pow(ord(char), e, n) for char in message]
    return ciphertext

# RSA Decryption
def decryption_algorithm(ciphertext, private_key):
    d, n = private_key
    plaintext = [chr(pow(char, d, n)) for char in ciphertext]
    return ''.join(plaintext)

#  usage

p, q = 73, 89  # Large prime numbers
public_key, private_key = generate_keys(p, q)

