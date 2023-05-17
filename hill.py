#kush code
# import numpy as np
# from functools import reduce

# def encrypt(msg):
#     # Replace spaces with nothing
#     msg = msg.replace(" ", "")
#     # Ask for keyword and get encryption matrix
#     C = make_key()
#     print(C)
#     # Append zero if the messsage isn't divisble by 2
#     len_check = len(msg) % 2 == 0
#     if not len_check:
#         msg += "0"
#     P = create_matrix_of_integers_from_string(msg)
#     msg_len = int(len(msg) / 2)
#     # Calculate P * C
#     encrypted_msg = ""
#     for i in range(msg_len):
#         # Dot product
#         row_0 = P[0][i] * C[0][0] + P[1][i] * C[0][1]
#         integer = int(row_0 % 26 + 65)
#         encrypted_msg += chr(integer)
#         row_1 = P[0][i] * C[1][0] + P[1][i] * C[1][1]
#         integer = int(row_1 % 26 + 65)
#         encrypted_msg += chr(integer)
#     return encrypted_msg

# def decrypt(encrypted_msg):
#     C = make_key()
#     # Inverse matrix
#     determinant = C[0][0] * C[1][1] - C[0][1] * C[1][0]
#     determinant = determinant % 26
#     multiplicative_inverse = find_multiplicative_inverse(determinant)
#     C_inverse = C
#     # Swap a <-> d
#     C_inverse[0][0], C_inverse[1][1] = C_inverse[1, 1], C_inverse[0, 0]
#     # Replace
#     C[0][1] *= -1
#     C[1][0] *= -1
#     for row in range(2):
#         for column in range(2):
#             C_inverse[row][column] *= multiplicative_inverse
#             C_inverse[row][column] = C_inverse[row][column] % 26

#     P = create_matrix_of_integers_from_string(encrypted_msg)
#     msg_len = int(len(encrypted_msg) / 2)
#     decrypted_msg = ""
#     for i in range(msg_len):
#         column_0 = P[0][i] * C_inverse[0][0] + P[1][i] * C_inverse[0][1]
#         integer = int(column_0 % 26 + 65)
#         decrypted_msg += chr(integer)
#         column_1 = P[0][i] * C_inverse[1][0] + P[1][i] * C_inverse[1][1]
#         integer = int(column_1 % 26 + 65)
#         decrypted_msg += chr(integer)
#     if decrypted_msg[-1] == "0":
#         decrypted_msg = decrypted_msg[:-1]
#     return decrypted_msg

# def find_multiplicative_inverse(determinant):
#     multiplicative_inverse = -1
#     for i in range(26):
#         inverse = determinant * i
#         if inverse % 26 == 1:
#             multiplicative_inverse = i
#             break
#     return multiplicative_inverse


# def make_key():
#     determinant = 0
#     C = None
#     while True:
#         # cipher = input("Input 4 letter cipher: ")
#         lst1 = [int(item) for item in input("Enter the list items : ").split()]
#         print("integer key", lst1)
#         cipher = ''
#         for i in lst1:
#          cipher+=chr(i+65)
#         C = create_matrix_of_integers_from_string(cipher)
#         determinant = C[0][0] * C[1][1] - C[0][1] * C[1][0]
#         determinant = determinant % 26
#         print("det",determinant)
#         inverse_element = find_multiplicative_inverse(determinant)
#         if inverse_element == -1:
#             print("Determinant is not relatively prime to 26, uninvertible key")
#         elif np.amax(C) > 26 and np.amin(C) < 0:
#             print("Only a-z characters are accepted")
#             print(np.amax(C), np.amin(C))
#         else:
#             break
#     return C

# def create_matrix_of_integers_from_string(string):
#     integers = [chr_to_int(c) for c in string]
#     length = len(integers)
#     M = np.zeros((2, int(length / 2)), dtype=np.int32)
#     iterator = 0
#     for column in range(int(length / 2)):
#         for row in range(2):
#             M[row][column] = integers[iterator]
#             iterator += 1
#     print("M", M)
#     return M

# def chr_to_int(char):
#     char = char.upper()
#     integer = ord(char) - 65
#     return integer


# if __name__ == "__main__":
#     msg = input("Message: ")
#     encrypted_msg = encrypt(msg)
#     print(encrypted_msg)
#     decrypted_msg = decrypt(encrypted_msg)
#     print(decrypted_msg)

#gfg
keyMatrix = [[0] * 3 for i in range(3)]
 
# Generate vector for the message
messageVector = [[0] for i in range(3)]
 
# Generate vector for the cipher
cipherMatrix = [[0] for i in range(3)]
 
# Following function generates the
# key matrix for the key string
def getKeyMatrix(key):
    k = 0
    for i in range(3):
        for j in range(3):
            keyMatrix[i][j] = ord(key[k]) % 65
            k += 1
 
# Following function encrypts the message
def encrypt(messageVector):
    for i in range(3):
        for j in range(1):
            cipherMatrix[i][j] = 0
            for x in range(3):
                cipherMatrix[i][j] += (keyMatrix[i][x] *
                                       messageVector[x][j])
            cipherMatrix[i][j] = cipherMatrix[i][j] % 26
 
def HillCipher(message, key):
 
    # Get key matrix from the key string
    getKeyMatrix(key)
 
    # Generate vector for the message
    for i in range(3):
        messageVector[i][0] = ord(message[i]) % 65
 
    # Following function generates
    # the encrypted vector
    encrypt(messageVector)
 
    # Generate the encrypted text
    # from the encrypted vector
    CipherText = []
    for i in range(3):
        CipherText.append(chr(cipherMatrix[i][0] + 65))
 
    # Finally print the ciphertext
    print("Ciphertext: ", "".join(CipherText))
 
# Driver Code
def main():
 
    # Get the message to
    # be encrypted
    message = "ACT"
 
    # Get the key
    key = "GYBNQKURP"
 
    HillCipher(message, key)
 
if __name__ == "__main__":
    main()
 
