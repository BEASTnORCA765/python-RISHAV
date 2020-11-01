import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
a = input().split(' ')
print(a)
sum = 0
for i in range(0,len(a),2):
    a[i]=int(a[i])
    sum = sum + a[i]
print("sum:", sum)


    
