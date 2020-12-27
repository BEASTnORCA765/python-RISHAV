import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w') 
a = int(input())
b = int(input())
for i in range(b):
    print(a,'*',i+1,'=',a*(i+1))