import numpy as np
import os
import cv2 
from skimage import color, io
from PIL import Image
import random
import matplotlib.pyplot as plt


def readImage(path):
	if os.path.isfile(path)==False:
		raise Exception("Invalid path for the file or the program doesn't have required permissions")
	try:
		img = cv2.imread(path)
	except Exception as i:
		raise i
	else:
		return img

def ApplyArnoldTransform(imageData):
    m = imageData.shape[0]
    n = imageData.shape[1]

    t = max(m,n)

    sampleImage = np.zeros([t,t,3])
    imagePadding = ((0,t-m),(0,t-n),(0,0))

    paddedImg = np.pad(imageData, imagePadding, mode='constant', constant_values=255)

    for i in range(0,t):
        for j in range(0,t):
            sampleImage[i][j] = paddedImg[(2*i+j)%t][(j+i)%t]

    return sampleImage

def ApplyInverseArnoldTransform(imageData):
    m = imageData.shape[0]
    n = imageData.shape[1]

    sampleImage = np.zeros([m,n,3])

    if m != n:
        raise Exception("Supplied Encrypted image is not a square image")

    for i in range(0 , m):
        for j in range(0, m):
            sampleImage[i][j] = imageData[(i-j)%m][((2*j)-i)%m]

    return sampleImage

def encryptImage(imageData, key):
    tempImg = imageData
    for i in range(0,key):
        tempImg = ApplyArnoldTransform(tempImg)
    imageData = tempImg
    return imageData

def decryptImage(imageData, key):
    tempImg = imageData
    for i in range(0,key):
        tempImg = ApplyInverseArnoldTransform(tempImg)
    imageData = tempImg     
    return imageData

cwd_path = os.getcwd()
print("path: ", cwd_path)

image_path = cwd_path+ '/rose.jpg'
key = 25

imgclr = readImage(image_path)
cv2.imshow('image view', imgclr)
cv2.waitKey(0)

EncryptedImageData = encryptImage(imgclr, key)
EncryptedWritePath = cwd_path+'/Arnold_Cat_Enc.png'
cv2.imwrite(EncryptedWritePath, EncryptedImageData)
EncryptedImageData = EncryptedImageData.astype(np.uint8)
cv2.imshow('Encrypted image view', EncryptedImageData)
cv2.waitKey(0)






cwd_path = os.getcwd()
print("path: ", cwd_path)
image_path = cwd_path + '/Arnold_Cat_Enc.png'
clrimg = io.imread(image_path)
imgplot = plt.imshow(clrimg)
plt.show()


imgclr_1D = clrimg.ravel() 


### GCD Function
def CalculateGcd(i,j):
    temp = i%j
    while(temp != 0):
        i = j
        j = temp
        temp = i%j

    return j
    

# Selecting the two Prime Numbers as Big as possible
p1 = 37
p2 = 23
n = p1*p2
totientValue = (p1-1)*(p2-1)

# Initially selecting a value of e between 1 and the totient value
e = random.randrange(1, totientValue)  
#Using GCD to verify if e and totient(phi(n)) are comprime or not
# If not select a new value of e
gcdVal = CalculateGcd(e, totientValue)
while gcdVal != 1:
    e = random.randrange(1, totientValue)
    gcdVal = CalculateGcd(e, totientValue)

# To find the  D Value  
def CalculateD(e, phi):
    d = 1
    temp = (d*e)%phi

    while (temp != 1):
        d += 1
        temp = (d*e)%phi

    return d


d = CalculateD(e, totientValue)


# Precompute Montgomery parameter r
r = 2**(len(bin(n))-2)

# Precompute Montgomery constant
r_inv = pow(r, -1, n)

# Encryption of the Image values present in the 1d vector using Montgomery modular exponentiation
ency = []
for i in range(0, len(imgclr_1D)):
    temp = pow((int(imgclr_1D[i]) * r) % n, e, n)
    ency.append(int((temp * r_inv) % n))

# Reshaping the 1d vector into the m*n*3 sized array
ency_clrimg = np.array(ency).reshape(clrimg.shape[0], clrimg.shape[1], clrimg.shape[2])
imgplot = plt.imshow(ency_clrimg)
plt.show()

# Decryption of the image using Montgomery modular exponentiation
dec_clr = []
for i in range(0, len(ency)):
    temp = pow((ency[i] * r) % n, d, n)
    dec_clr.append(int((temp * r_inv) % n))

#Decrypted Image
decy_img = np.array(dec_clr).reshape(clrimg.shape[0], clrimg.shape[1], clrimg.shape[2])
imgplot = plt.imshow(decy_img)
plt.show()







DecryptedImageData = decryptImage(decy_img, key)
DecryptedWritePath = cwd_path+'/Arnold_Cat_Dec.png'
cv2.imwrite(DecryptedWritePath, DecryptedImageData)
DecryptedImageData = DecryptedImageData.astype(np.uint8)
cv2.imshow('Decrypted image view', cv2.cvtColor(DecryptedImageData, cv2.COLOR_BGR2RGB))
cv2.waitKey(0)




