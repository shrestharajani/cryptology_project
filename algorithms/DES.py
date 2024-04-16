# Data Encryption Standard (DES) Implementation

# Initial and final permutation tables
IP = [
    58, 50, 42, 34, 26, 18, 10, 2,
    60, 52, 44, 36, 28, 20, 12, 4,
    62, 54, 46, 38, 30, 22, 14, 6,
    64, 56, 48, 40, 32, 24, 16, 8,
    57, 49, 41, 33, 25, 17, 9, 1,
    59, 51, 43, 35, 27, 19, 11, 3,
    61, 53, 45, 37, 29, 21, 13, 5,
    63, 55, 47, 39, 31, 23, 15, 7
]

IP_INV = [
    40, 8, 48, 16, 56, 24, 64, 32,
    39, 7, 47, 15, 55, 23, 63, 31,
    38, 6, 46, 14, 54, 22, 62, 30,
    37, 5, 45, 13, 53, 21, 61, 29,
    36, 4, 44, 12, 52, 20, 60, 28,
    35, 3, 43, 11, 51, 19, 59, 27,
    34, 2, 42, 10, 50, 18, 58, 26,
    33, 1, 41, 9, 49, 17, 57, 25
]

# Expansion table
EXPANSION_TABLE = [
    32, 1, 2, 3, 4, 5,
    4, 5, 6, 7, 8, 9,
    8, 9, 10, 11, 12, 13,
    12, 13, 14, 15, 16, 17,
    16, 17, 18, 19, 20, 21,
    20, 21, 22, 23, 24, 25,
    24, 25, 26, 27, 28, 29,
    28, 29, 30, 31, 32, 1
]

# S-boxes
S_BOXES = [
    [
        # S-box 1
        [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
        # S-box 2
        [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
        # S-box 3
        [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
        # S-box 4
        [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]
    ],
    # Define more S-boxes as needed
]

# Permutation table
PERMUTATION_TABLE = [
    16, 7, 20, 21,
    29, 12, 28, 17,
    1, 15, 23, 26,
    5, 18, 31, 10,
    2, 8, 24, 14,
    32, 27, 3, 9,
    19, 13, 30, 6,
    22, 11, 4, 25
]

# Initial key permutation table
PC1 = [
    57, 49, 41, 33, 25, 17, 9,
    1, 58, 50, 42, 34, 26, 18,
    10, 2, 59, 51, 43, 35, 27,
    19, 11, 3, 60, 52, 44, 36,
    63, 55, 47, 39, 31, 23, 15,
    7, 62, 54, 46, 38, 30, 22,
    14, 6, 61, 53, 45, 37, 29,
    21, 13, 5, 28, 20, 12, 4
]

# Key permutation table for generating round keys
PC2 = [
    14, 17, 11, 24, 1, 5, 3, 28,
    15, 6, 21, 10, 23, 19, 12, 4,
    26, 8, 16, 7, 27, 20, 13, 2,
    41, 52, 31, 37, 47, 55, 30, 40,
    51, 45, 33, 48, 44, 49, 39, 56,
    34, 53, 46, 42, 50, 36, 29, 32
]

# Key shift schedule
KEY_SHIFTS = [
    1, 1, 2, 2, 2, 2, 2, 2,
    1, 2, 2, 2, 2, 2, 2, 1
]

def initial_permutation(block):
    return permute(block, IP)

def final_permutation(block):
    return permute(block, IP_INV)

def permute(block, table):
    return ''.join(block[i - 1] for i in table if i <= len(block))

def generate_subkeys(key):
    print("Key:", key)
    print("PC1 Table:", PC1)
    key = permute(key, PC1)
    subkeys = []
    left, right = key[:28], key[28:]
    for shift in KEY_SHIFTS:
        left = shift_left(left, shift)
        right = shift_left(right, shift)
        subkeys.append(permute(left + right, PC2))
    return subkeys

def shift_left(bits, n):
    return bits[n:] + bits[:n]

def expansion(block):
    return permute(block, EXPANSION_TABLE)

def s_box_substitution(bits):
    output = ''
    for i in range(0, len(bits), 6):
        block = bits[i:i + 6]
        row = int(block[0] + block[5], 2)
        col = int(block[1:5], 2)
        val = S_BOXES[i // 6][row][col]
        output += format(val, '04b')
    return output

def f_function(expanded, subkey):
    print("Expanded:", expanded)
    print("Subkey:", subkey)
    xored = ''.join(str(int(expanded[i]) ^ int(subkey[i])) for i in range(48))
    print("Xored:", xored)
    substituted = s_box_substitution(xored)
    return permute(substituted, P_BOX)

def encrypt_block(block, subkeys):
    block = initial_permutation(block)
    left, right = block[:32], block[32:]
    for subkey in subkeys:
        left, right = right, ''.join(str(int(left[i]) ^ int(f_function(right, subkey)[i])) for i in range(32))
    return final_permutation(right + left)

def encryption_algorithm(plaintext, key):
    key_use = key[:8] if len(key) > 8 else key + '0' * (8 - len(key))
    subkeys = generate_subkeys(key_use)
    plaintext_bits = ''.join(format(ord(char), '08b') for char in plaintext)
    padded_length = (len(plaintext_bits) + 64 - 1) // 64 * 64
    plaintext_bits = plaintext_bits.ljust(padded_length, '0')
    ciphertext = ''
    for i in range(0, len(plaintext_bits), 64):
        ciphertext += encrypt_block(plaintext_bits[i:i + 64], subkeys)
    return ciphertext


   
    
