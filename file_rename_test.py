import os
import glob

print(os.getcwd())
l=[]

path = "C:\\Users\\ayari\\Pictures\\ayari"
for i in range(1):
    l=glob.glob("C:\\Users\\ayari\\Pictures\\ayari\\*")
print(l)

name="C:\\Users\\ayari\\Pictures\\ayari\\IMG_"

for i in range(1):
    os.rename (l[i] , name + str(i)+".jpg")
