def key_to_matrix_generation(plain_key):
    key = plain_key.upper().replace(" ", "")
    key_length = len(key)
    matrix_size = int(key_length ** 0.5)
    if matrix_size ** 2 != key_length:
        raise ValueError("Key length must be a perfect square")

    key_matrix = []
    for i in range(matrix_size):
        row = []
        for j in range(matrix_size):
            index = i * matrix_size + j
            row.append(ord(key[index]) - ord('A'))
        key_matrix.append(row)
    return key_matrix

def encryption_algorithm(plain_text,plain_key):
    matrik_key = key_to_matrix_generation(plain_key)
    matrix_size = len(matrik_key)
    plain_text = plain_text.upper().replace(" ", "")
    encrypted_text = ""
    if len(plain_text) % matrix_size != 0:
        plain_text += 'X' * (matrix_size - len(plain_text) % matrix_size)
    
    for i in range(0, len(plain_text), matrix_size):
        plain_text_matrix = []
        for j in range(matrix_size):
            plain_text_matrix.append(ord(plain_text[i + j]) - ord('A'))
        encrypted_text_matrix = [0] * matrix_size
        
        for j in range(matrix_size):
            for k in range(matrix_size):
                encrypted_text_matrix[j] +=  plain_text_matrix[k]*matrik_key[k][j] 
            encrypted_text_matrix[j] %= 26
        
        for x in encrypted_text_matrix:
            encrypted_text += chr(x + ord('A'))
    return encrypted_text

def decryption_algorithm(encrypted_text,cipher_key):
    matrik_key = key_to_matrix_generation(cipher_key)
    matrix_size = len(matrik_key)
    ciphertext = encrypted_text.upper().replace(" ", "")

    ciphertext_matrix = []
    
    for i in range(0, len(ciphertext), matrix_size):
    #     for j in range(matrix_size):
    #         ciphertext_matrix.append(ord(ciphertext[i + j]) - ord('A'))
    # print("Cipher",ciphertext_matrix)
        cipher_slice = ciphertext[i:i+matrix_size]
        cipher_slice_indices = [ord(char) - ord('A') for char in  cipher_slice]
        ciphertext_matrix.append(cipher_slice_indices)

    decrypted_text = ""
    det = determinant(matrik_key)
    det_inv = pow(det, -1, 26)
    adjoint_matrix = adjoint(matrik_key)
    
    key_inverse = []
    for i in range(matrix_size):
        row = []
        for j in range(matrix_size):
            row.append((det_inv * adjoint_matrix[i][j]) % 26)
        key_inverse.append(row)
    
    for group in ciphertext_matrix:
        decrypted_group = []
        for j in range(matrix_size):
            sum_value = 0
            for i in range(matrix_size):
                sum_value += group[i] * key_inverse[j][i]
            decrypted_group.append(sum_value % 26)
        decrypted_text += ''.join([chr(int(char) + ord('A')) for char in decrypted_group])
    return decrypted_text

# Function to calculate determinant of a matrix
def determinant(matrix):
    n = len(matrix)
    if n == 1:
        return matrix[0][0]
    det = 0
    for j in range(n):
        det += (-1) ** j * matrix[0][j] * determinant(minor(matrix, 0, j))
    return det

# Function to calculate minor of a matrix
def minor(matrix, row, col):
    result = []
    for i in range(len(matrix)):
        if i != row:
            result_row = []
            for j in range(len(matrix)):
                if j != col:
                    result_row.append(matrix[i][j])
            result.append(result_row)
    return result

# Function to calculate adjoint of a matrix
def adjoint(matrix):
    n = len(matrix)
    adj_matrix = []
    for i in range(n):
        row = []
        for j in range(n):
            sign = (-1) ** (i + j)
            minor_det = determinant(minor(matrix, i, j))
            row.append(sign * minor_det)
        adj_matrix.append(row)
    return adj_matrix
    
            
   