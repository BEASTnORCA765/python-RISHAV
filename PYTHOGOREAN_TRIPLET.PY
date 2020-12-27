import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w') 
def pythogoras(a):
    if a[0]**2 + a[1]**2==a[2]**2:
        print("pythogorean triplet confirmed")
    else:
        print("no triplet")
a = input().split()
a=[int(i) for i in a]
pythogoras(a)



