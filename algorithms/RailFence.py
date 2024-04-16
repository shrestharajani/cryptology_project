def encryption_algorithm(plain_text,rails):
    fence = [[] for _ in range(rails)]
    rail = 0
    direction = 1

    for char in plain_text:
        fence[rail].append(char)
        rail += direction

        if rail == rails - 1 or rail == 0:
            direction *= -1

    ciphertext = ''.join([char for rail in fence for char in rail])
    return ciphertext

def decryption_algorithm(encrypted_text,rails):
    fence = [[] for _ in range(rails)]
    rail = 0
    direction = 1

    for char in encrypted_text:
        fence[rail].append(None)
        rail += direction

        if rail == rails - 1 or rail == 0:
            direction *= -1

    index = 0
    for rail in range(rails):
        for i in range(len(fence[rail])):
            fence[rail][i] = encrypted_text[index]
            index += 1
            rail += direction
            if rail == rails - 1 or rail == 0:
                direction *= -1

    plaintext = ''.join([char for rail in fence for char in rail])
    return plaintext