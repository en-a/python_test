import math
import sys

n=sys.argv[1]
m=sys.argv[2]

if 2**int(n)>math.factorial(int(m)):
    print("Exponential")
else :
    print("Factorial")