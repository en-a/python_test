import csv
r=0
g=0
b=0

#それぞれのカウント
bc=0  
yc=0
row=[]

def csvreader_b(x):
    with open('myfile.csv') as f:
        reader = csv.reader(f)
        l = [row for row in reader] 
        r=int(l[x][0])
        g=int(l[x][1])
        b=int(l[x][2])
        #print(l[x])
    bb=0
    
    if g-b < 20 and r-b < 60:
        #print("ブルーベース ")
        bb+=1
        #print(c)
        return bb
        
    else:
        #print("イエローベース")
        bb+=0
        return bb

def csvreader_y(x):
    with open('myfile.csv') as f:
        reader = csv.reader(f)
        l = [row for row in reader] 
        r=int(l[x][0])
        g=int(l[x][1])
        b=int(l[x][2])
        #print(l[x])
    yy=0
    if g-b < 20 and r-b < 60:
        #print("ブルーベース")
        yy+=0
        #print(c)
        return yy
            
    else:
        #print("イエローベース")
        yy+=1
        return yy

for i in range(1,20):
    bb=csvreader_b(i)
    bc+=bb

for i in range(22,41):
    yy=csvreader_y(i)
    yc+=yy

print("ブルーベースの確率",bc/20*100)
print("イエローベースの確率",yc/20*100)