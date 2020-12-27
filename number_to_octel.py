import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w') 
a = int(input())
b = []
while a>0:
    f = a%8
    b.append(f)
    a = a//8
for i in reversed(b):
    print(i,end="") 