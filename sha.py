import hashlib

def generate_hash(message):
    # Create a new SHA-256 hash object
    hasher = hashlib.sha256()
    # Update the hash object with the message
    hasher.update(message.encode('utf-8'))
    # Get the hexadecimal representation of the hash
    hashed_message = hasher.hexdigest()
    return hashed_message

# Get plaintext input from the user
plaintext = input("Enter plaintext: ")

# Sender generates hash of the message
hash_sender = generate_hash(plaintext)
print("Sender's hashed message:", hash_sender)

# Sender sends the message and hash to Receiver
received_message = plaintext
received_hash = hash_sender

# Receiver receives the message and calculates the hash
calculated_hash = generate_hash(received_message)

# Compare the calculated hash with the received hash
if calculated_hash == received_hash:
    print("Message integrity verified. The message has not been tampered with.")
else:
    print("Message integrity compromised. The message may have been tampered with.")
