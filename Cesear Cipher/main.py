alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


word = "The Romans are coming tomorrow to destroy you"
code = 4


def encryptword(word, code):
    encrypted = ""

    for char in word:
        if char != " ":
            indexofword = alphabets.index(char.upper())
            if indexofword + code >= len(alphabets):
                newindex = (indexofword+code)- len(alphabets)
            else:
                newindex = indexofword+code
            encryptedchar = alphabets[newindex]
            if char.islower():
                encryptedchar = encryptedchar.lower()
            else:
                encryptedchar = encryptedchar.upper()
            encrypted = encrypted + encryptedchar
        else:
            encrypted = encrypted + char

    return encrypted
    
print("Encrypted word", encryptword(word, 4))

decrypt = encryptword(word, 4)
print(decrypt)

def decryptword(word, code):
    decrypted = ""

    for char in decryptword:
        if char != " ":
            indexofword = alphabets.index(char.upper())
            newindex = indexofword - code
            decryptedchar = alphabets[newindex]
            if char.islower():
                decryptedchar = decryptedchar.lower()
            else:
                decryptedchar = decryptedchar.upper()
            decrypted = decrypted + decryptedchar
        else:
            decrypted = decrypted + char

    return decrypted


# decryptword(decrypt, 4)



