import itertools
n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=list(map(int,input().split()))

for team in itertools.combinations(a,2):
    print(team)


m=0
j=0
i=list(itertools.product(range(1,4)))
print(i)
for m in n:
   a[i]=b[c[j]]
   m+=1
print(m)