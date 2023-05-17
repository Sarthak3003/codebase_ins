import math

def encryption(a, b, pt):
    ct = ''
    
    for i in range(0, len(pt)):
        ct += chr(math.ceil(math.fmod(a * (ord(pt[i]) - 65) + b, 26)) + 65)

    return ct

def decryption(a, b, ct):
    pt = ''

    c = pow(a, -1, 26)
    c = mod_fn(c, 26)

    for i in range(0, len(ct)):
        modulo = math.fmod(c * (ord(ct[i]) - 65 - b), 26)

        if (modulo < 0):
            modulo = 26 + modulo

        pt += chr(math.ceil(modulo) + 65)

    return pt

def mod_fn(a, n):
    return a % n

plaintext = input('Plain Text: ')
a = int(input('a: '))
b = int(input('b: '))

ciphertext = encryption(a, b, plaintext)
print('Cipher Text:', ciphertext)

plaintext = decryption(a, b, ciphertext)
print('Plain Text:', plaintext)