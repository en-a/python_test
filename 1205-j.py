import os
import glob

print(os.getcwd())
l=[]

path = "F:\\JPG\\*"
for i in range(2619):
    l=glob.glob("F:\\JPG\\*")
#print(l)

name="F:\\JPG\\IMG_"

for i in range(2619):
    os.rename (l[i] , name + str(i)+".jpg")

print("finish")