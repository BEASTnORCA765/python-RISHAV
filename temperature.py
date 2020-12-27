import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w') 
a = input()
b = a[-1]
a = a[:-1]
a = float(a)
if b == 'C':
    c = a
    f = 9/5 * a+32
    k = a + 273.15
    print("{} C\n{} F\n{} K".format(round(c,2),round(f,2),round(k,2)))
elif b == 'F':
    c = 5/9 * (a-32)
    f = a
    k = a + 273.15
    print("{} C\n{} F\n{} K".format(round(c,2),round(f,2),round(k,2)))
elif b == 'K':
    c = a - 273.15
    f =  9/5 * (a - 273.15)+32
    k = a
    print("{} C\n{} F\n{} K".format(round(c,2),round(f,2),round(k,2)))