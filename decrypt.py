
from PIL import Image
import numpy as np
inimg=Image.open(r'C:\Users\Home\Pictures\gvr enc.png')
img=np.asarray(inimg,dtype='uint8').copy()
x,y,z=img.shape
text=""
def decrypt():
    global text
    for i in range(x):
        for j in range(y):
            for k in range(z):
                if (img[i][j]==[0,0,0]).all():
                    return 1
                text+=chr(img[i][j][k])
                
decrypt()
print(text)
#author-@_._hello_world._._
