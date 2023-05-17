
#PLAYFAIR CIPHER - with numbers 

from itertools import zip_longest
from functools import reduce

n = 0

def chunk_string(string, chunk_size):
    for i in range(0, len(string), chunk_size):
      print(string[i:i+chunk_size])
    return [string[i:i+chunk_size] for i in range(0, len(string), chunk_size)]

def generate_key(key):
    key = key.upper()
    key = "".join(sorted(set(key), key=key.index))
    key += "".join(chr(i) for i in range(65, 91) if chr(i) not in key)
    key += "".join(chr(i) for i in range(48, 58))
    p = chunk_string(key, 6)
    # print("Key: ", chunk_string(key, 6))
    return key

def split_pairs(message):
    message = message.upper().replace(" ", "")
    message = [c1+c2 if c2  else c1+"XX" for c1, c2 in zip_longest(message[::2], message[1::2])]
    return message

def get_indices(char, key):
    index = key.index(char)
    row, col = index // 6, index % 6
    return row, col

def encrypt(message, key):
    
    key = generate_key(key)
    message = split_pairs(message)

    def encrypt_digraph(digraph):
        (r1, c1), (r2, c2) = get_indices(digraph[0], key), get_indices(digraph[1], key)
        if r1 == r2:
            return key[r1*6 + (c1+1)%6] + key[r2*6 + (c2+1)%6]
        elif c1 == c2:
            return key[((r1+1)%6)*6 + c1] + key[((r2+1)%6)*6 + c2]
        else:
            return key[r1*6 + c2] + key[r2*6 + c1]

    ciphertext = reduce(lambda x, y: x + y, [encrypt_digraph(d) for d in message])
    print('Encrypted Ciphertext: ', ciphertext)
    return ciphertext

def decrypt(ciphertext, key):
    key = generate_key(key)

    def decrypt_digraph(digraph):
        (r1, c1), (r2, c2) = get_indices(digraph[0], key), get_indices(digraph[1], key)
        if r1 == r2:
            return key[r1*6 + (c1-1)%6] + key[r2*6 + (c2-1)%6]
        elif c1 == c2:
            return key[((r1-1)%6)*6 + c1] + key[((r2-1)%6)*6 + c2]
        else:
            return key[r1*6 + c2] + key[r2*6 + c1]

    plaintext = reduce(lambda x, y: x + y, [decrypt_digraph(d) for d in split_pairs(ciphertext)])
    return plaintext.lower().replace("x", "")

# plain_text = "jazz"
# key = "monarchy"
plain_text = input("Enter plain text: ")
# n = plain_text.index(' ')
key = input("Enter key: ")
print('<-----ENCRYPTION----->')
ct = encrypt(plain_text, key)
print('<-----DECRYPTION----->')
dt = decrypt(ct, key)
output = dt[:n] + ' ' + dt[n:]
print("Decrypted Plain Text: ", output)

# enter 2 words w space uske liye bhi chalega and they will like, for eg: hello world


#PLAYFAIR - without numbers
def playfair(pt, key):     
    grid = [[0 for i in range(5)] for j in range(5)] 
    key_list = list(dict.fromkeys(key))     
    alphabet = "abcdefghijklmnopqrstuvwxyz"     
    pt = pt.lower() 
    ct = "" 
    de = "" 
 
    empty = False     
    for i in range(5):         
        for j in range(5):             
            if not key_list:                 
                empty = True 
                break             
            grid[i][j] = key_list.pop(0)         
        if empty:             
            break 
 
    for letter in "".join(list(dict.fromkeys(key))): 
        alphabet = alphabet.replace(letter, "") 
 
    idx = 0     
    for i in range(5):         
        for j in range(5):             
            if grid[i][j] == 0: 
                al_letter = alphabet[idx]                 
                if al_letter == 'i':                     
                    grid[i][j] = "i"                     
                    idx += 2                 
                else: 
                    grid[i][j] = al_letter                     
                    idx += 1 
 
    idx = 0     
    while idx < len(pt): 
        first = pt[idx]         
        if idx == len(pt)-1: 
            pt += 'x'             
            idx += 2             
            continue         
        second = pt[idx+1]         
        if first == second:             
            pt = pt[:idx+1] + "x" + pt[idx+1:]         
        idx += 2 
 
    pt_list = [pt[i:i+2] for i in range(0, len(pt), 2)] 
 
    for pair in pt_list: 
        row1, col1 = [(index, row.index(pair[0])) for index, row in enumerate(grid) if pair[0] in row][0] 
        row2, col2 = [(index, row.index(pair[1])) for index, row in enumerate(grid) if pair[1] in row][0] 
 
        if row1 == row2: 
            ct += grid[row1][(col1+1) % 5] + grid[row1][(col2+1) % 5]         
        elif col1 == col2: 
            ct += grid[(row1+1) % 5][col1] + grid[(row2+1) % 5][col1]         
        else: 
            ct += grid[row1][col2] + grid[row2][col1] 
 
    print("Encrypted text: ", ct) 
 
    ct_list = [ct[i:i + 2] for i in range(0, len(ct), 2)] 
 
    for pair in ct_list: 
        row1, col1 = [(index, row.index(pair[0])) for index, row in enumerate(grid) if pair[0] in row][0] 
        row2, col2 = [(index, row.index(pair[1])) for index, row in enumerate(grid) if pair[1] in row][0] 
 
        if row1 == row2: 
            de += grid[row1][(col1-1) % 5] + grid[row1][(col2-1) % 5]         
        elif col1 == col2: 
            de += grid[(row1-1) % 5][col1] + grid[(row2-1) % 5][col1]         
        else: 
            de += grid[row1][col2] + grid[row2][col1] 
 
    print("Decrypted Text: ", de) 
 
 
plaintext = input("Enter Plaintext: ") 
key = input("Enter Key: ")  
playfair(plaintext, key) 