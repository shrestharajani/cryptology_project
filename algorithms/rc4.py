
def rc4_ksa(key):
    S = list(range(256))
    j = 0
    for i in range(256):
        j = (j + S[i] + key[i % len(key)]) % 256
        S[i], S[j] = S[j], S[i]
    return S

def rc4_prga(S, plaintext):
    """Pseudo-Random Generation Algorithm (PRGA) for RC4"""
    ciphertext = []
    i, j = 0, 0
    for char in plaintext:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        K = S[(S[i] + S[j]) % 256]
        ciphertext.append(char ^ K)
    return bytes(ciphertext)

def encryption_algorithm(plaintext,key):
    """Encrypt plaintext using RC4 algorithm"""
    S = rc4_ksa(list(key.encode()))
    prga = rc4_prga(S, plaintext.encode())
    return prga.hex()

def decryption_algorithm(ciphertext,key):
    ciphertext = bytes.fromhex(ciphertext)
    """Decrypt ciphertext using RC4 algorithm"""
    S = rc4_ksa(list(key.encode()))
    prga = rc4_prga(S, ciphertext).decode()
    return ' '.join(prga.strip("[]'").replace("'","").split(','))

# plaintext = ''.join(str(input("Enter PlainText: ").lower().split()))
# key = input("Enter key: ")

# ciphertext = encrypt(plaintext,key)
# print(ciphertext)

# # Decryption
# decrypted_text =decrypt(ciphertext,key)
# print(decrypted_text)
