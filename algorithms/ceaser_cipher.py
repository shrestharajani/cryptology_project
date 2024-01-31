
def encryption_algorithm():
    plain_text = input("Enter the plain text: ")
    encrypted_text = ""
    for character in plain_text:
        if character.isalpha():
            if character.islower():
                # ord(a) = 97 (ASCII value)
                # For the case of lowercase characters
                encrypted_character = (((ord(character)-ord('a'))+3)%26)+ord('a')
            else:
                # ord(A) = 65 (ASCII value)
                # For the case of uppercase characters
                encrypted_character = (((ord(character)-ord('A'))+3)%26)+ord('A')
            encrypted_text += chr(encrypted_character)
        else:
            encrypted_text += character
    return encrypted_text

def decryption_algorithm(encrypted_text):
    decrypted_text = ""
    for character in encrypted_text:
        if character.isalpha():
            if character.islower():
                # ord(a) = 97 (ASCII value)
                # For the case of lowercase characters
                decrypted_character = (((ord(character)-ord('a'))-3)%26)+ord('a')
            else:
                # ord(A) = 65 (ASCII value)
                # For the case of uppercase characters
                decrypted_character = (((ord(character)-ord('A'))-3)%26)+ord('A')
            decrypted_text += chr(decrypted_character)
        else:
            decrypted_text += character
    return decrypted_text
            
   