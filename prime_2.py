import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
a=int(input())
b=int(input())
import math
for j in range(a,b+1):
    q=int(math.sqrt(j))
    if j==1:
        print(j)
        exit()
    p = 1
    for i in range(2,q+1):
        if j%i==0:
            p=0
            break
    if p==1:
        print(j)
    