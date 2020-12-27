import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w') 
a = input().split('_')
print(a)
for i in a:
    print(i.title(),end="")
    
    
