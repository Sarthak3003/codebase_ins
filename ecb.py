def text_to_binary(text):
    # Convert plaintext to binary string
    return ''.join(format(ord(c), '08b') for c in text)

def binary_to_text(binary):
    # Convert binary string to plaintext
    return ''.join(chr(int(binary[i:i+8], 2)) for i in range(0, len(binary), 8))

def ecb_encrypt(plaintext, key, t, mode):
    # Convert plaintext to binary
    binary_plaintext = text_to_binary(plaintext)

    # Pad the binary plaintext to a multiple of 128 bits
    padding_length = 128 - len(binary_plaintext) % 128
    binary_plaintext += '0' * padding_length

    # Split binary plaintext into 128-bit blocks
    blocks = [binary_plaintext[i:i+128] for i in range(0, len(binary_plaintext), 128)]

    # Encrypt each block using ECB mode and key
    ciphertext_blocks = []
    for block in blocks:
        if mode == 'left':
            block = block[t:] + block[:t]  # Shift t bits to the left
        elif mode == 'right':
            block = block[-t:] + block[:-t]  # Shift t bits to the right

        

        ciphertext_blocks.append(block)

    # Concatenate the ciphertext blocks and convert to plaintext
    ciphertext_binary = ''.join(ciphertext_blocks)
    ciphertext = binary_to_text(ciphertext_binary)

    return ciphertext

# Example usage
plaintext = "This is a sample plaintext to be encrypted using ECB mode."
key = "secretkey"
t = 3
mode = 'left'

ciphertext = ecb_encrypt(plaintext, key, t, mode)

print("Plaintext: ", plaintext)
print("Ciphertext:", ciphertext)

def ecb_decrypt(ciphertext, key, t, mode):
    # Convert ciphertext to binary
    binary_ciphertext = text_to_binary(ciphertext)

    # Split binary ciphertext into 128-bit blocks
    blocks = [binary_ciphertext[i:i+128] for i in range(0, len(binary_ciphertext), 128)]

    # Decrypt each block using ECB mode and key
    plaintext_blocks = []
    for block in blocks:
        decrypted_block = block
        if mode == 'left':
            decrypted_block = decrypted_block[-t:] + decrypted_block[:-t]  # Shift t bits to the right
        elif mode == 'right':
            decrypted_block = decrypted_block[t:] + decrypted_block[:t]  # Shift t bits to the left

        plaintext_blocks.append(decrypted_block)

    # Concatenate the decrypted blocks and convert to plaintext
    plaintext_binary = ''.join(plaintext_blocks)
    plaintext = binary_to_text(plaintext_binary)

    return plaintext

# Example usage
decrypted_text = ecb_decrypt(ciphertext, key, t, mode)

print("Ciphertext:", ciphertext)
print("Decrypted text:", decrypted_text)