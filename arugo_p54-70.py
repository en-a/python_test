l=[70,98,92,88,64]
total=0
for i in l:
    total+=i
print("合計=",total)
print("平均=",total/5)
#-----------------------
total_1=0
for i in range(1,11):
    total_1+=i
print(total_1)
#-----------------------
def goukei(n):
    a=0
    for i in range(1,n+1):
        a+=i
       # print(a)
    return a
print(goukei(10))
#------------------------
for i in range(1,10):
    k=""
    for j in range(1,10):       
        k+="{}x{}={:2d} ".format(j,i,i*j)
        #2桁のd(10進数)
    print(k)
#------------------------

for i in range(2,101):
    for j in range(2,i//2+1):
        if i%j==0:
            break
    else:
        print(i,end=",")
#-----------------------

