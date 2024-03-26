def generate_key():
    # Generate a key for Monoalphabetic Cipher with a +3 shift
    # return ('zrusiwmolbethnvafcjdgpkyqx')
    import string
    alphabet = list(string.ascii_uppercase)
    shifted_alphabet = alphabet[3:] + alphabet[:3]
    return dict(zip(alphabet, shifted_alphabet))

def encryption_algorithm(plain_text):
    # Encrypt the given plain text using the provided key
    key=generate_key()
    cipher_text = ''
    for char in plain_text:
        if char.isalpha():
            # Preserve the case
            is_upper = char.isupper()
            char = char.upper()

            # Encrypt the character
            if char in key:
                cipher_char = key[char]
                cipher_text += cipher_char.upper() if is_upper else cipher_char.lower()
            else:
                cipher_text += char

        else:
            # Preserve non-alphabetic characters
            cipher_text += char
    return cipher_text

def decryption_algorithm(cipher_text):
    key=generate_key()
    # Decrypt the given cipher text using the provided key
    inverse_key = {v: k for k, v in key.items()}
    plain_text = ''
    for char in cipher_text:
        if char.isalpha():
            # Preserve the case
            is_upper = char.isupper()
            char = char.upper()

            # Decrypt the character
            if char in inverse_key:
                plain_char = inverse_key[char]
                plain_text += plain_char.upper() if is_upper else plain_char.lower()
            else:
                plain_text += char

        else:
            # Preserve non-alphabetic characters
            plain_text += char
    return plain_text