def prepare_input(text):
    # Remove spaces and convert to uppercase
    text = text.replace(" ", "").upper()
    # Replace 'J' with 'I' (standard convention)
    text = text.replace("J", "I")
    # Insert filler ('X') between repeated letters
    text_with_filler = ""
    i = 0
    while i < len(text):
        text_with_filler += text[i]
        if i < len(text) - 1 and text[i] == text[i + 1]:
            text_with_filler += 'X'
            i += 1  # Skip the next letter
        i += 1
    # If the length of the text with filler is odd, add an extra 'X' at the end
    if len(text_with_filler) % 2 != 0:
        text_with_filler += 'X'
    # Split the text into pairs of letters
    pairs = [text_with_filler[i:i+2] for i in range(0, len(text_with_filler), 2)]
    return pairs

def generate_table(key):
    # Create a matrix (5x5) for the Playfair cipher table
    table = []
    # Fill it with unique letters from the keyword followed by the rest of the alphabet
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ" # J is omitted
    key = key.upper()
    for char in key:
        if char not in table and char in alphabet:
            table.append(char)
            alphabet = alphabet.replace(char, "")
    # Fill the remaining spaces in the table with the remaining letters of the alphabet
    for char in alphabet:
        table.append(char)
    # Reshape the list into a 5x5 matrix
    return [table[i:i+5] for i in range(0, 25, 5)]

def find_position(table, letter):
    # Find the position of a letter in the table
    for i in range(5):
        for j in range(5):
            if table[i][j] == letter:
                return i, j

def encryption_algorithm(plaintext, key):
    # Prepare input
    plaintext_pairs = prepare_input(plaintext)
    # Generate the Playfair table
    table = generate_table(key)
    # Encrypt pairs
    ciphertext = ""
    for pair in plaintext_pairs:
        # Get the positions of both letters in the table
        row1, col1 = find_position(table, pair[0])
        row2, col2 = find_position(table, pair[1])
        # Apply Playfair rules to find the new letters
        if row1 == row2:  # Same row
            ciphertext += table[row1][(col1 + 1) % 5] + table[row2][(col2 + 1) % 5]
        elif col1 == col2:  # Same column
            ciphertext += table[(row1 + 1) % 5][col1] + table[(row2 + 1) % 5][col2]
        else:  # Different row and column
            ciphertext += table[row1][col2] + table[row2][col1]
    return ciphertext

def decryption_algorithm(ciphertext, key):
    # Prepare input
    ciphertext_pairs = prepare_input(ciphertext)
    # Generate the Playfair table
    table = generate_table(key)
    # Decrypt pairs
    plaintext = ""
    for pair in ciphertext_pairs:
        # Get the positions of both letters in the table
        row1, col1 = find_position(table, pair[0])
        row2, col2 = find_position(table, pair[1])
        # Apply Playfair rules to find the new letters
        if row1 == row2:  # Same row
            plaintext += table[row1][(col1 - 1) % 5] + table[row2][(col2 - 1) % 5]
        elif col1 == col2:  # Same column
            plaintext += table[(row1 - 1) % 5][col1] + table[(row2 - 1) % 5][col2]
        else:  # Different row and column
            plaintext += table[row1][col2] + table[row2][col1]
    return plaintext