import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w') 
a = int(input())
l1 = []
while a>0:
    c = a%2
    l1.append(c)
    a = a//2
for i in reversed(l1):
    print(i,end = '')


