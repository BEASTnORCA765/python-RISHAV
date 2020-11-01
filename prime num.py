import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
a=int(input())
import math
q=int(math.sqrt(a))
if a==1:
    print("nor prime or composite number")
    exit()
p = 1
for i in range(2,q+1):
    if a%i==0:
        p=0
        break
if p==1:
    print("prime number confirmed")
else :
    print("not a prime number")








