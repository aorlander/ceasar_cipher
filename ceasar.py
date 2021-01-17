def encrypt(key,plaintext):
    ciphertext = ''
    for c in plaintext:
        ciphertext = ciphertext + chr((ord(c) + key - 65) % 26 + 65)
    print(ciphertext)
    return ciphertext

def decrypt(key,ciphertext):
    plaintext = ""
    
    return plaintext
