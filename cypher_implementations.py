def caesar_encryption(plaintext, key):
    ciphertext = ""
    for i in range(len(plaintext)):
        if plaintext[i].isalpha():
            if plaintext[i].isupper():
                ciphertext += chr((ord(plaintext[i]) + key - 65) % 26 + 65)
            else:
                ciphertext += chr((ord(plaintext[i]) + key - 97) % 26 + 97)
        else:
            ciphertext += plaintext[i]
    return ciphertext

def caesar_decryption(ciphertext, key):
    plaintext = ""
    for i in range(len(ciphertext)):
        if ciphertext[i].isalpha():
            if ciphertext[i].isupper():
                plaintext += chr((ord(ciphertext[i]) - key - 65) % 26 + 65)
            else:
                plaintext += chr((ord(ciphertext[i]) - key - 97) % 26 + 97)
        else:
            plaintext += ciphertext[i]
    return plaintext


print(caesar_encryption("Hello World!", 3))
print(caesar_decryption("Khoor Zruog!", 3))