
from PIL import Image
import numpy as np
inimg=Image.open(r'C:\Users\Home\Pictures\gvr.jpg')
img=np.asarray(inimg).copy()
x,y,z=img.shape
text="Guido van Rossum is a Dutch programer best known as the creator of the Python programming language"
c=0
def encrypt():
    global c,img
    for i in range(x):
        for j in range(y):
            for k in range(z):
            
                if c==len(text):
                    img[i][j+1]=[0,0,0]
                    return 1
                
                img[i][j][k]=ord(text[c])
                c+=1
encrypt()
opimg=Image.fromarray(img)
opimg.show()
opimg.save(r'C:\Users\Home\Pictures\gvr enc.png')
#author-@_._hello_world._._

