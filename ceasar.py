def encrypt(key,plaintext):
    ciphertext = ""
    for c in plaintext:
        ciphertext = ciphertext + chr((ord(c) + key - 65) % 26 + 65)
    return ciphertext

def decrypt(key,ciphertext):
    plaintext = ""
    for c in ciphertext:
        plaintext = plaintext + chr((ord(c) - key - 65) % 26 + 65)
    return plaintext
