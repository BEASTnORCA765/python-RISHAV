import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w') 
rows = int(input())
character = input()
for i in range(rows):
    for j in range(i+1,0,-1):
        print(character,end=' ')
    print()
