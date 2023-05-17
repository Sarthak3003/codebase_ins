import math
def encrypt(message, keyword):
    message = message.upper().replace(" ", "")
    keyword = keyword.upper()
    key_table = sorted(keyword)
    copy_key = keyword
    rows =  int(math.ceil(float(len(message)) / len(keyword)))
    cols = len(keyword)

    matrix = []
    for i in range(rows):
        col = [0] * cols
        matrix.append(col)
    
    if (len(message) < rows*cols):
        while len(message) != rows*cols:
            message += "X"
    print("18", message)
    for i in range(len(message)):
        row = i//cols 
        col = i%cols
        matrix[row][col] = message[i]
    ciphertext = ""

    for i in range(len(keyword)):
        index = copy_key.index(key_table[i])
        copy_key = copy_key.replace(key_table[i], "8", 1)
        for j in range(rows):
            ciphertext += matrix[j][index]
    return ciphertext

def decrypt(message, keyword):
    message = message.upper().replace(" ", "")
    keyword = keyword.upper()
    key_table = sorted(keyword)
    copy_key = keyword
    rows =  int(math.ceil(float(len(message)) / len(keyword)))
    cols = len(keyword)

    matrix = []
    for i in range(rows):
        col = [0] * cols
        matrix.append(col)
    index = 0
    for i in range(cols):
        cindex = copy_key.index(key_table[i])
        copy_key = copy_key.replace(key_table[i], "9", 1)
        for j in range(rows):
            matrix[j][cindex] = message[index]
            index += 1
    decrypted_message = ""
    for i in range(rows):
        for j in range(cols):
            decrypted_message += matrix[i][j]
    decrypted_message.rstrip("X")
    return decrypted_message
msg = 'we are the best'
print("Message", msg.upper().replace(" ", ""))
keyword = "HEAVEN"
enc = encrypt(msg, keyword)
print("Encrypted Message:", enc)
dec = decrypt(enc, keyword)
print("Decrypted Message:", dec)