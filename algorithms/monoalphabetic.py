def generate_key():
    import random
    import string

    # Generating a shuffled version of the alphabet
    alphabet = list(string.ascii_lowercase)
    random.shuffle(alphabet)
    
    # Creating a dictionary to map each letter to its corresponding shuffled letter
    key = {}
    for i in range(26):
        key[string.ascii_lowercase[i]] = alphabet[i]
    
    return key

def encryption_algorithm(plaintext, key):
    ciphertext = ''
    for char in plaintext:
        if char.isalpha():
            if char.isupper():
                # If the character is uppercase, encrypt it and maintain its case
                ciphertext += key[char.lower()].upper()
            else:
                # If the character is lowercase, encrypt it
                ciphertext += key[char]
        else:
            # If the character is not alphabetic, leave it unchanged
            ciphertext += char
    return ciphertext

def decryption_algorithm(ciphertext, key):
    plaintext = ''
    for char in ciphertext:
        if char.isalpha():
            if char.isupper():
                # If the character is uppercase, decrypt it and maintain its case
                plaintext += list(key.keys())[list(key.values()).index(char.lower())].upper()
            else:
                # If the character is lowercase, decrypt it
                plaintext += list(key.keys())[list(key.values()).index(char)]
        else:
            # If the character is not alphabetic, leave it unchanged
            plaintext += char
    return plaintext
