import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w') 
class people:
    def __init__(self,name,age,Aadhar):
        self.name = name
        self.age = age
        self.Aadhar = Aadhar
    def check_eligibility(self):
        if self.age>=128:
            print(self.name,"You have won guiness book of world records")
        elif self.age>=18 and self.Aadhar == "yes":
            print(self.name,"Konichiwa ! You are eligible")
        elif self.age>=18 and self.Aadhar == "no":
            print(self.name,"pehle apna aadhar banwaa ****")
        else:
            print(self.name,"Tu abhi chota hain")
if __name__ == "__main__":
    n = int(input())
    for j in range(n):
        a = input().split()
        b = []
        a[1] = int(a[1])
        stu = people(a[0],a[1],a[2])
        stu.check_eligibility()



       