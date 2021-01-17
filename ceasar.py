def encrypt(key,plaintext):
    ciphertext = plaintext
    for c in ciphertext:
        ciphertext[c] = chr(ord(c) + key) 
    print(ciphertext)
    return ciphertext

def decrypt(key,ciphertext):
    plaintext = ciphertext
    for c in plaintext:
        plaintext[c] = chr(ord(c) - key)
    print(plaintext)
    return plaintext
