import math

def rsaAlgo(pi, qi, msg):
    n = pi * qi
    phi = (pi - 1) * (qi - 1)
    e = 2
    
    while (e < phi):
        if(multiplicative_inverse(e, phi) == 1):
            break
        else:
            e = e + 1
            
    k = 2
    d = (1 + (k*phi))/e
    
    c = pow(msg, e)
    c = math.fmod(c, n)
    print("Encrypted Data:", c)
    
    m = pow(c, d)
    m = math.fmod(m, n)
    print("Decrypted Data:", msg)
    
def multiplicative_inverse(number, modulus):
    for i in range(1, modulus):
        if (number * i) % modulus == 1:
            return i
    return None    

p = int(input('P: '))
q = int(input('Q: '))
m = int(input('Message: '))

rsaAlgo(p, q, m)