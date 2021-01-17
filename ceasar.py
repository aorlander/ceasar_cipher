def encrypt(key,plaintext):
    ciphertext = ""
    for c in plaintext:
        ciphertext[c] = chr(ord(c) + key) 
    print(ciphertext)
    return ciphertext

def decrypt(key,ciphertext):
    plaintext = ""
    for c in ciphertext:
        plaintext[c] = chr(ord(c) - key)
    print(plaintext)
    return plaintext
