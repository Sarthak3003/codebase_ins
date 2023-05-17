import random
import cv2
import numpy as np
im = cv2.imread('1-strawberry-png-images.png')
res, im_png = cv2.imencode('.png', im)
img_png_bytes=im_png.tobytes()
with open('initial_static.png', 'wb') as f:
    f.writelines(im_png)
with open("original_text.txt",'w') as f:
    f.writelines(str(im_png))  
encrypt_matrix=[]
for i in im_png:
    encrypt_matrix.append(int(i))
with open("original_text.txt",'w') as f:
    f.writelines(str(encrypt_matrix))
key=[]
num=[29,31]    
for _ in range(len(encrypt_matrix)):
    key.append(random.randint(1,100))
remainder_all=[]
quotient_all=[]
quotient=[]
remainder=[]
for i in range(len(encrypt_matrix)):
    encrypt_matrix[i]+=key[i]
    quotient.append(int(encrypt_matrix[i]//num[0]))
    remainder.append(encrypt_matrix[i]%num[0])
    encrypt_matrix[i]%=num[0]
remainder_all.append(remainder)
remainder=[]
quotient_all.append(quotient)
quotient=[]
for i in range(len(encrypt_matrix)):
    encrypt_matrix[i]+=key[i]
    quotient.append(int(encrypt_matrix[i]//num[1]))
    remainder.append(encrypt_matrix[i]%num[1])
    encrypt_matrix[i]%=num[1]
remainder_all.append(remainder)
quotient_all.append(quotient)

decrypt_matrix=[]
for i in range(len(key)):
    decrypt_matrix.append(num[1]*quotient_all[1][i]+remainder_all[1][i])
for i in range(len(key)):
    decrypt_matrix[i]-=key[i]
    decrypt_matrix[i]+=num[0]*quotient_all[0][i]
    decrypt_matrix[i]-=key[i]  
# print(encrypt_matrix==decrypt_matrix)
with open("d1.txt",'w') as f:
    f.writelines(str(decrypt_matrix))
with open("q1.txt",'w') as f:
    f.writelines(str(quotient_all)) 
with open("cipher.txt",'w') as f:
    f.writelines(str(encrypt_matrix))

for i in range(len(encrypt_matrix)):
    encrypt_matrix[i]=int(encrypt_matrix[i])
encrypt_matrix_numpy=np.array(encrypt_matrix)
encrypt_matrix_numpy_int8=encrypt_matrix_numpy.astype(np.uint8)
encrypt_bytes=encrypt_matrix_numpy_int8.tobytes()
with open('encrypted_image.png', 'wb') as f:
    f.write(encrypt_bytes)

with open("original_key.txt",'w') as f:
    f.writelines(str(key))
for i in range(len(decrypt_matrix)):
    decrypt_matrix[i]=int(decrypt_matrix[i])
decrypt_matrix_numpy=np.array(decrypt_matrix)
decrypt_matrix_numpy_int8=decrypt_matrix_numpy.astype(np.uint8)
decrypted_bytes=decrypt_matrix_numpy_int8.tobytes()
with open('final1_my_image.png', 'wb') as f:
    f.write(decrypted_bytes)

print(img_png_bytes==decrypted_bytes)
