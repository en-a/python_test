irasa1900# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 15:17:34 2021

@author: ayari
"""

import csv
h=0
s=0
v=0

#それぞれのカウント
bc=0  
yc=0
row=[]

def csvreader_b(x):
    with open('myfile2.csv') as f:
        reader = csv.reader(f)
        l = [row for row in reader] 
        h=float(l[x][0])
        s=float(l[x][1])
        v=float(l[x][2])
        #print(l[x])
    bb=0
    
    if s>37.0 and v<93.0:
        #print("yベース ")
        bb+=1
        #print(c)
        return bb
     
    elif s>37.0 and v>93.0:
        #print("bベース")
        bb+=1
        return bb
    
    else:
       #print("yベース ")
        bb+=0
        #print(c)
        return bb

def csvreader_y(x):
    with open('myfile2.csv') as f:
        reader = csv.reader(f)
        l = [row for row in reader] 
        h=float(l[x][0])
        s=float(l[x][1])
        v=float(l[x][2])
        #print(l[x])
    yy=0
    if s<37.0 and v<93.0:
        #print("yベース")
        yy+=1
        #print(c)
        return yy
            
    if s<37.0 and v>93.0:
        #print("yベース")
        yy+=1
        #print(c)
        return yy
    
    else:
        #print("bベース")
        yy+=0
        return yy

for i in range(1,20):
    bb=csvreader_b(i)
    bc+=bb

for i in range(22,41):
    yy=csvreader_y(i)
    yc+=yy

print("ブルーベースの確率",bc/20*100)
print("イエローベースの確率",yc/20*100)