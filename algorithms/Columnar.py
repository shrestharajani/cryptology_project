import math

def encryption_algorithm(plain_text,key):
    encrypted_text = ""
    
    #track key indices
    key_indx = 0
    
    plaintext_length = float(len(plain_text))
    plaintext_list = list(plain_text)
    key_list = sorted(list(key))
    
    #calculate column of the matrix
    col = len(key)
    
    #calculate maximum row of the matrix
    row = int(math.ceil(plaintext_length/col))
    
    #add the padding character '_' in empty
    #the empty cell of the matrix
    fill_null = int((row*col) - plaintext_length)
    plaintext_list.extend('_' * fill_null)
    
    #create Matrix and insert message and
    #padding characters row-wise
    matrix = [plaintext_list[i : i + col] for i in range(0, len(plaintext_list), col)]
    
    #read matrix column-wise using key
    for _ in range(col):
        curr_idx = key.index(key_list[key_indx])
        encrypted_text += ''.join([row[curr_idx] for row in matrix])
        key_indx += 1
    return encrypted_text

def decryption_algorithm(cipher_text,key):
    decrypted_text = ""
    
    #track key indices
    key_indx = 0
    
    #track msg indices
    msg_indx = 0
    cipher_length = float(len(cipher_text))
    cipher_list = list(cipher_text)
    
    #calculate column of the matrix
    col = len(key)
    
    #calculate maximum row of the matrix
    row = int(math.ceil(cipher_length/col))
    
    #convert key into list and sort
    #alphabetically so we can access
    #each character by its alphabetical position.
    key_list = sorted(list(key))
    
    #create an empty matrix to
    #store deciphered message
    dec_cipher = []
    for _ in range(row):
        dec_cipher +=[[None] * col]
        
    #Arrange the matrix column wise according
    #to permutation order by adding into new matrix
    for _ in range(col):
        curr_idx = key.index(key_list[key_indx])
        
        for j in range(row):
            dec_cipher[j][curr_idx] = cipher_list[msg_indx]
            msg_indx += 1
        key_indx += 1
        
    #convert decrypted msg matrix into a string
    try:
        decrypted_text = ''.join(sum(dec_cipher,[]))
    except TypeError:
        raise TypeError("This program cannot","handle repeating words.")
        
    null_count = decrypted_text.count('_')
    
    if null_count>0:
        return decrypted_text[: -null_count]
    
    return decrypted_text




    