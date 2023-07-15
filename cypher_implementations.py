import math
import random


def caesar_encryption(plaintext, key):
    """Implements the Caesar cipher encryption algorithm.

    Args:
        plaintext (str): The plaintext to encrypt.
        key (int): The amount of steps to shift each character by.

    Returns:
        str: The encrypted text.
    """
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
    """ Implements the Caesar cipher decryption algorithm.

    Args:
        ciphertext (str): The ciphertext to decrypt.
        key (int): The amount of steps to shift each character by.

    Returns:
        str: The decrypted text.
    """
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

def rail_fence_encryption(plaintext, rails):
    """Implements the rail fence cipher encryption algorithm.

    Args:
        plaintext (str): The plaintext to encrypt.
        rails (int): The number of rails to use.

    Returns:
        str: The encrypted text.
    """
    fence = [['.' for _ in range(len(plaintext))] for _ in range(rails)]
    rail = 0
    direction = 1  # Direction: 1 for down, -1 for up
    
    for i in range(len(plaintext)):
        fence[rail][i] = plaintext[i]
        rail += direction
        
        # Change direction when reaching the top or bottom rail
        if rail == 0 or rail == rails - 1:
            direction *= -1
    
    ciphertext = ''
    
    for rail in range(rails):
        for i in range(len(plaintext)):
            if fence[rail][i] != '.':
                ciphertext += fence[rail][i]
    
    return ciphertext

def rail_fence_decryption(ciphertext, rails):
    """Implements the rail fence cipher decryption algorithm.

    Args:
        ciphertext (str): The ciphertext to decrypt.
        rails (int): The number of rails to use.

    Returns:
        str: The decrypted text.
    """
    fence = [['.' for _ in range(len(ciphertext))] for _ in range(rails)]
    rail = 0
    direction = 1  # Direction: 1 for down, -1 for up
    
    for i in range(len(ciphertext)):
        fence[rail][i] = '*'
        rail += direction
        
        # Change direction when reaching the top or bottom rail
        if rail == 0 or rail == rails - 1:
            direction *= -1
    
    index = 0
    plaintext = ''
    
    for rail in range(rails):
        for i in range(len(ciphertext)):
            if fence[rail][i] == '*' and index < len(ciphertext):
                fence[rail][i] = ciphertext[index]
                index += 1
    
    rail = 0
    direction = 1
    
    for i in range(len(ciphertext)):
        plaintext += fence[rail][i]
        rail += direction
        
        # Change direction when reaching the top or bottom rail
        if rail == 0 or rail == rails - 1:
            direction *= -1
    
    return plaintext

def rotary_enigma_encrypt(plaintext, key):
    """Implements the rotary enigma encryption algorithm.

    Args:
        plaintext (str): The plaintext to encrypt.
        key (int): The key to use.

    Returns:
        str: The encrypted text.
    """
    random.seed(key)
    rotors_seed = [random.randint(1, 2**32-1) for _ in range(3)] # 32 bits of entropy
    rotors = [[i for i in range(26)] for _ in range(3)]
    for i in range(3):
        random.seed(rotors_seed[i])
        random.shuffle(rotors[i])

    random.seed(key)
    ciphertext = ""

    rotors_counters = [0 for _ in range(3)]
    
    for char in plaintext:
        if not char.isalpha():
            ciphertext += char
        else:
            char_value = ord(char.lower()) - ord('a')
            char_value = (char_value + rotors[0][rotors_counters[0]]) % 26
            char_value = (char_value + rotors[1][rotors_counters[1]]) % 26
            char_value = (char_value + rotors[2][rotors_counters[2]]) % 26
            cipherchar = chr(char_value + ord('a'))
            ciphertext += cipherchar.upper() if char.isupper() else cipherchar

            rotors[0][rotors_counters[0]] = (rotors[0][rotors_counters[0]] + 1) % 26
            if rotors[0][rotors_counters[0]] == 0:
                rotors[1][rotors_counters[1]] = (rotors[1][rotors_counters[1]] + 1) % 26
                if rotors[1][rotors_counters[1]] == 0:
                    rotors[2][rotors_counters[2]] = (rotors[2][rotors_counters[2]] + 1) % 26

    return ciphertext

def rotary_enigma_decrypt(ciphertext, key):
    """Implements the rotary enigma decryption algorithm.

    Args:
        ciphertext (str): The ciphertext to decrypt.
        key (int): The key to use.

    Returns:
        str: The decrypted text.
    """
    random.seed(key)
    rotors_seed = [random.randint(1, 2**32-1) for _ in range(3)] # 32 bits of entropy
    rotors = [[i for i in range(26)] for _ in range(3)]
    for i in range(3):
        random.seed(rotors_seed[i])
        random.shuffle(rotors[i])

    random.seed(key)
    plaintext = ""

    rotors_counters = [0 for _ in range(3)]
    
    for char in ciphertext:
        if not char.isalpha():
            plaintext += char
        else:
            char_value = ord(char.lower()) - ord('a')
            char_value = (char_value - rotors[2][rotors_counters[2]]) % 26
            char_value = (char_value - rotors[1][rotors_counters[1]]) % 26
            char_value = (char_value - rotors[0][rotors_counters[0]]) % 26
            plainchar = chr(char_value + ord('a'))
            plaintext += plainchar.upper() if char.isupper() else plainchar

            rotors[0][rotors_counters[0]] = (rotors[0][rotors_counters[0]] + 1) % 26
            if rotors[0][rotors_counters[0]] == 0:
                rotors[1][rotors_counters[1]] = (rotors[1][rotors_counters[1]] + 1) % 26
                if rotors[1][rotors_counters[1]] == 0:
                    rotors[2][rotors_counters[2]] = (rotors[2][rotors_counters[2]] + 1) % 26

    return plaintext

def get_text_from_file(filename):
    """Reads the contents of a file and returns it as a string.

    Args:
        filename (str): The name of the file to read.

    Returns:
        str: The contents of the file.
    """
    with open(filename, "r") as file:
        return file.read()

# Main method
def main():
    # Read the plaintext from the file
    plaintext = get_text_from_file("plaintext.txt")

    # Encrypt the plaintext using the Caesar cipher
    ciphertext = caesar_encryption(plaintext, 3)

    # Write the ciphertext to a file
    with open("caesarCrypto.txt", "w") as file:
        file.write(ciphertext)

    # Read the ciphertext from the file
    ciphertext = get_text_from_file("caesarCrypto.txt")

    # Decrypt the ciphertext using the Caesar cipher
    plaintext = caesar_decryption(ciphertext, 3)

    # Write the plaintext to a file
    with open("caesarPlain.txt", "w") as file:
        file.write(plaintext)

    # Encrypt the plaintext using the rail fence cipher
    ciphertext = rail_fence_encryption(plaintext, 3)

    # Write the ciphertext to a file
    with open("railCrypto.txt", "w") as file:
        file.write(ciphertext)

    # Read the ciphertext from the file
    ciphertext = get_text_from_file("railCrypto.txt")

    # Decrypt the ciphertext using the rail fence cipher
    plaintext = rail_fence_decryption(ciphertext, 3)

    # Write the plaintext to a file
    with open("railPlain.txt", "w") as file:
        file.write(plaintext)

    # Encrypt the plaintext using the rotary enigma cipher
    ciphertext = rotary_enigma_encrypt(plaintext, 3)

    # Write the ciphertext to a file
    with open("enigmaCrypto.txt", "w") as file:
        file.write(ciphertext)

    # Read the ciphertext from the file
    ciphertext = get_text_from_file("enigmaCrypto.txt")

    # Decrypt the ciphertext using the rotary enigma cipher
    plaintext = rotary_enigma_decrypt(ciphertext, 3)

    # Write the plaintext to a file
    with open("enigmaPlain.txt", "w") as file:
        file.write(plaintext)

if __name__ == "__main__":
    main()