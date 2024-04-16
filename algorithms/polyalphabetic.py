def generate_vigenere_table():
    table = {}
    for i in range(26):
        table[chr(ord('A') + i)] = {}
        for j in range(26):
            table[chr(ord('A') + i)][chr(ord('A') + j)] = chr(((i + j) % 26) + ord('A'))
    return table

def encryption_algorithm(plaintext, key):
    table = generate_vigenere_table()
    ciphertext = ""
    key_index = 0
    for char in plaintext.upper():
        if char.isalpha():
            ciphertext += table[key[key_index]][char]
            key_index = (key_index + 1) % len(key)
        else:
            ciphertext += char
    return ciphertext

def decryption_algorithm(ciphertext, key):
    table = generate_vigenere_table()
    plaintext = ""
    key_index = 0
    for char in ciphertext.upper():
        if char.isalpha():
            for k, v in table[key[key_index]].items():
                if v == char:
                    plaintext += k
                    break
            key_index = (key_index + 1) % len(key)
        else:
            plaintext += char
    return plaintext