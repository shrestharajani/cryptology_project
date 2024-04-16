import secrets

def generate_key(length):
    # Generate a random key of specified length using cryptographically secure random number generator
    key = ''.join(secrets.choice('01') for _ in range(length))
    return key

def encryption_algorith(plaintext, key):
    ciphertext = ''
    for i in range(len(plaintext)):
        # XOR each character of plaintext with corresponding bit of the key
        encrypted_char = chr(ord(plaintext[i]) ^ int(key[i]))
        ciphertext += encrypted_char
    return ciphertext

def decryption_algorithm(ciphertext, key):
    plaintext = ''
    for i in range(len(ciphertext)):
        # XOR each character of ciphertext with corresponding bit of the key
        decrypted_char = chr(ord(ciphertext[i]) ^ int(key[i]))
        plaintext += decrypted_char
    return plaintext
