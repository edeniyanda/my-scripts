alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"



def encrypt_word(word, code):
    encrypted = ""

    for char in word:
        if char != " ":
            original_index = alphabets.index(char.upper())
            if original_index + code >= len(alphabets):
                new_index = (original_index+code)- len(alphabets)
            else:
                new_index = original_index+code
            encryptedchar = alphabets[new_index]
            if char.islower():
                encryptedchar = encryptedchar.lower()
            encrypted = encrypted + encryptedchar
        else:
            encrypted = encrypted + char

    return encrypted
    

def decrypt_word(word, code):
    decrypted = ""

    for char in word:
        if char != " ":
            original_index = alphabets.index(char.upper())
            newindex = original_index - code
            decryptedchar = alphabets[newindex]
            if char.islower():
                decryptedchar = decryptedchar.lower()
            decrypted = decrypted + decryptedchar
        else:
            decrypted = decrypted + char

    return decrypted


print("Welcome to the Encryption and Decryption Program!")
print("You can encrypt or decrypt any message you want.")
print("Type 'Q' at any time to quit.")


while True:
    action = input("\nWould you like to (E)ncrypt or (D)ecrypt a message? ").upper()
        
    if action == 'Q':
        print("Goodbye!")
        break
    elif action not in ['E', 'D']:
        print("Invalid choice. Please enter 'E' to encrypt, 'D' to decrypt, or 'Q' to quit.")
        continue
    
    word = input("Enter the word or sentence: ")
    try:
        code = int(input("Enter the code (a number) to use for encryption/decryption: "))
    except ValueError:
        print("Invalid input. Please enter a valid number for the code.")
        continue

    if action == 'E':
        encrypted_message = encrypt_word(word, code)
        print(f"Encrypted Message: {encrypted_message}")
    elif action == 'D':
        decrypted_message = decrypt_word(word, code)
        print(f"Decrypted Message: {decrypted_message}")
