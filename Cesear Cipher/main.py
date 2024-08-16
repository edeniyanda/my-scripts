alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


word = "Eden is a bo"
code = 4

encrypted = ""

for char in word:
    if char != " ":
        indexofword = alphabets.index(char.upper())
        if indexofword + code >= len(alphabets):
            overflow = (indexofword+code)- len(alphabets)
            print(overflow)
            newindex = overflow
            print(newindex)
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
print(encrypted)






