import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
pro = 1
a = input().split()
# print(a)
for i in range(0,len(a),2):
    a[i]=int(a[i])
    pro=pro*a[i]
print("product:",pro)




