def prepare_text(plaintext):
    plaintext = plaintext.replace(" ", "").upper()  # Remove spaces and convert to uppercase
    plaintext = plaintext.replace("J", "I")  # Replace 'J' with 'I' (since Playfair does not use 'J')
    # Split the plaintext into pairs of letters (digraphs)
    digraphs = []
    i = 0
    while i < len(plaintext):
        if i == len(plaintext) - 1 or plaintext[i] == plaintext[i + 1]:
            # If the last letter is alone or there are two identical consecutive letters,
            # append 'X' to make a digraph
            digraphs.append(plaintext[i] + 'X')
            i += 1
        else:
            digraphs.append(plaintext[i] + plaintext[i + 1])
            i += 2
    return digraphs

def generate_key_matrix(key):
    key_matrix = [['' for _ in range(5)] for _ in range(5)]
    letters = "ABCDEFGHIKLMNOPQRSTUVWXYZ"  # Omitting 'J' as it is usually combined with 'I' in Playfair
    key = key.replace(" ", "").upper()  # Remove spaces and convert to uppercase
    key = key.replace("J", "I")  # Replace 'J' with 'I'
    key += letters  # Append the rest of the alphabet to the key
    key = ''.join(dict.fromkeys(key))  # Remove duplicate letters

    # Fill the key matrix with the letters from the key
    i, j = 0, 0
    for letter in key:
        key_matrix[i][j] = letter
        j += 1
        if j == 5:
            j = 0
            i += 1
            if i == 5:
                break

    return key_matrix

def find_position(matrix, letter):
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == letter:
                return i, j

def encryption_algorithm(plaintext, key):
    digraphs = prepare_text(plaintext)
    key_matrix = generate_key_matrix(key)
    ciphertext = ''
    for digraph in digraphs:
        # Find positions of letters in the digraph
        row1, col1 = find_position(key_matrix, digraph[0])
        row2, col2 = find_position(key_matrix, digraph[1])
        # If the letters are in the same row, replace them with the letters to their right (circularly)
        if row1 == row2:
            ciphertext += key_matrix[row1][(col1 + 1) % 5] + key_matrix[row2][(col2 + 1) % 5]
        # If the letters are in the same column, replace them with the letters below them (circularly)
        elif col1 == col2:
            ciphertext += key_matrix[(row1 + 1) % 5][col1] + key_matrix[(row2 + 1) % 5][col2]
        # If the letters form a rectangle, replace them with the letters at the same row but the other corner of the rectangle
        else:
            ciphertext += key_matrix[row1][col2] + key_matrix[row2][col1]
    return ciphertext

def decryption_algorithm(ciphertext, key):
    key_matrix = generate_key_matrix(key)
    plaintext = ''
    for i in range(0, len(ciphertext), 2):
        # Find positions of letters in the digraph
        row1, col1 = find_position(key_matrix, ciphertext[i])
        row2, col2 = find_position(key_matrix, ciphertext[i + 1])
        # If the letters are in the same row, replace them with the letters to their left (circularly)
        if row1 == row2:
            plaintext += key_matrix[row1][(col1 - 1) % 5] + key_matrix[row2][(col2 - 1) % 5]
        # If the letters are in the same column, replace them with the letters above them (circularly)
        elif col1 == col2:
            plaintext += key_matrix[(row1 - 1) % 5][col1] + key_matrix[(row2 - 1) % 5][col2]
        # If the letters form a rectangle, replace them with the letters at the same row but the other corner of the rectangle
        else:
            plaintext += key_matrix[row1][col2] + key_matrix[row2][col1]
    plaintext = plaintext.replace('X', '')  # Remove any 'X' characters that were added during encryption
    # Remove any 'X' characters at the end if they were not originally present in the plaintext
    if len(plaintext) % 2 != 0:
        plaintext = plaintext[:-1]
    return plaintext
