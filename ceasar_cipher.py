def encrypt(key,plaintext):
    ciphertext=plaintext
    for c in ciphertext:
        new_c = c + key;
        print(new_c)
    return ciphertext

def decrypt(key,ciphertext):
    plaintext=""
    return plaintext

print("HELLO")