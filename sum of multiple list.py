import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w') 
n = int(input())
sum1=0
for i in range(n):
    temp = [int(i) for i in input().split()]
    sum1+=sum(temp)
print(sum1)




