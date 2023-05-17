import hashlib

def calculate_hash(message):
    sha1 = hashlib.sha1()
    sha1.update(message.encode())
    return sha1.hexdigest()

def verify_integrity(message, hash_value):
    calculated_hash = calculate_hash(message)
    if calculated_hash == hash_value:
        print("Integrity verified: Message has not been tampered with.")
    else:
        print("Integrity check failed: Message may have been tampered with.")


message = "Hello, World!"
hash_value = "0a0a9f2a6772942557ab5355d76af442f8f65e01"

calculated_hash = calculate_hash(message)
print("Calculated Hash:", calculated_hash)

verify_integrity(message, hash_value)