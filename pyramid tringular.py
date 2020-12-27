import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
rows = int(input())
character = input()
for i in range(rows):
    for j in range(rows-i,0,-1):
        print(" ",end=' ')
    for k in range(2*i+1):
        print(character,end=' ')
    print()
for i in range(rows):
    print(end='  ')
    for j in range(i+1):
        print(' ',end=' ')
    for k in range(2*(rows-i-1)-2,-1,-1):
        print(character,end=' ')
    print()   

    
      
    
