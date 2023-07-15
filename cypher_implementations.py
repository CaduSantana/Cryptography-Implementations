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




print(caesar_encryption("Hello World!", 3))
print(caesar_decryption((caesar_encryption("Hello World!", 3)), 3))
print(rail_fence_encryption("Hello World!", 3))
print(rail_fence_decryption((rail_fence_encryption("Hello World!", 3)), 3))