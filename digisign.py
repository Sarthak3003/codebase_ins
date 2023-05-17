# #OPTION 1
# import hashlib
# # import pycryptodomex as Crypto
# from Crypto.PublicKey import RSA
# from Crypto.Signature import PKCS1_v1_5
# from Crypto.Hash import SHA256

# def generate_key():
#     # Generate a new RSA key pair
#     key = RSA.generate(2048)
#     return key

# def sign_message(private_key, message):
#     # Sign a message using the private key
#     signer = PKCS1_v1_5.new(private_key)
#     h = SHA256.new(message.encode('utf-8'))
#     signature = signer.sign(h)
#     return signature

# def verify_signature(public_key, message, signature):
#     # Verify the signature of a message using the public key
#     verifier = PKCS1_v1_5.new(public_key)
#     h = SHA256.new(message.encode('utf-8'))
#     return verifier.verify(h, signature)

# # Example usage
# private_key = generate_key()
# public_key = private_key.publickey()
# message = "Hello, World!"

# signature = sign_message(private_key, message)
# valid = verify_signature(public_key, message, signature)

# print("Signature verified:", valid)



# # OPTION 2

# # !pip install pycryptodome
# # !pip install ecdsa

from ecdsa import SigningKey
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto import Random
from hashlib import sha256
import base64
def rsakeys():  
    length=1024  
    privatekey = RSA.generate(length, Random.new().read)  
    publickey = privatekey.publickey()  
    return privatekey, publickey


def encrypt(rsa_publickey,plain_text):
    cipher = PKCS1_OAEP.new(rsa_publickey)
    cipher_text=cipher.encrypt(plain_text)
    print("Encrypted msg - ",cipher_text)
    return cipher_text

def decrypt(rsa_privatekey,b64cipher):
    cipher = PKCS1_OAEP.new(rsa_privatekey)
    plaintext = cipher.decrypt(b64cipher)
    print("Decrypted msg - ",plaintext)
    return plaintext

msg = b'hello world'
print("Initial msg : ",msg)
privAlice,pubAlice = rsakeys()
print("A's Public key : ",pubAlice)
print("A's Private key : ",privAlice)
privBob,pubBob = rsakeys()
print("B's Public key : ",pubBob)
print("B's Private key : ",privBob)

encryptedMsg = encrypt(pubBob,msg)
hash = sha256(msg).hexdigest()
res = bytes(hash, 'utf-8')
private_key = SigningKey.generate()
vk = private_key.verifying_key
signature = private_key.sign(res)
print("signature: ",signature)

#decryption
decryptedMsg = decrypt(privBob,encryptedMsg)
hash = sha256(decryptedMsg).hexdigest()
res = bytes(hash, 'utf-8')
print(vk.verify(signature,res))