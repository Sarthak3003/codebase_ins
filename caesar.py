pt = input("Enter plain text: ")
k = int(input("Enter key: "))

ct=''

for i in pt:
    if i.isdigit():
        ct += chr((ord(i) + k - ord('0'))%9 + ord('0'))
    elif i.isalpha():
        if i.isupper():
            ct += chr(((ord(i)+k)-ord('A'))%26+ord('A'))
        else:
            ct += chr(((ord(i)+k)-ord('a'))%26+ord('a'))
    
print("Caesar cipher cipher text: ", ct)

pt2 = ''
for i in ct:
    if i.isdigit():
        pt2 += chr((ord(i) - k - ord('0'))%9 + ord('0'))
    elif i.isalpha():
        if i.isupper():
            pt2 += chr(((ord(i)-k)-ord('A'))%26+ord('A'))
        else:
            pt2 += chr(((ord(i)-k)-ord('a'))%26+ord('a'))
print("Decrypted text: ", pt2)

