import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w') 
a = [int(i) for i in input().split()]
max_num = a[0]
for i in range(len(a)):
    if a[i] > max_num:
        max_num = a[i]
print (max_num)