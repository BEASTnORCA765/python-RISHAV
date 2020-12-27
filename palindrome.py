import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w') 
a = input()
b = a[::-1]
print(a,b)
if a == b:
    print("palindrome confirmed")
else :
    print("not a palindrome")

