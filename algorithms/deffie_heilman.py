import random

# Prime number and generator
p = 23
g = 5

def generate_keys():
    # Sender's private key
    sender_private = random.randint(1, p)
    # Receiver's private key
    receiver_private = random.randint(1, p)

    # Calculate public keys
    sender_public = (g ** sender_private) % p
    receiver_public = (g ** receiver_private) % p

    # Shared secret calculation
    shared_secret_sender = (receiver_public ** sender_private) % p
    shared_secret_receiver = (sender_public ** receiver_private) % p

    return sender_private, receiver_private, sender_public, receiver_public, shared_secret_sender, shared_secret_receiver

def encryption_algorithm(plaintext, shared_key):
    encrypted_text = ""
    for char in plaintext:
        encrypted_text += chr(ord(char) + shared_key)
    return encrypted_text

def decryption_algorithm(encrypted_text, shared_key):
    decrypted_text = ""
    for char in encrypted_text:
        decrypted_text += chr(ord(char) - shared_key)
    return decrypted_text

# Diffie-Hellman key exchange
sender_private, receiver_private, sender_public, receiver_public, shared_secret_sender, shared_secret_receiver = generate_keys()

#print("Sender's private key:", sender_private)
#print("Receiver's private key:", receiver_private)
#print("Sender's public key:", sender_public)
#print("Receiver's public key:", receiver_public)
#print("Shared secret (Sender's side):", shared_secret_sender)
#print("Shared secret (Receiver's side):", shared_secret_receiver)



