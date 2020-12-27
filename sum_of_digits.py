import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w') 
a = [int(i) for i in list(input())]
print(sum(a))
