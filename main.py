import math


def enterRationFun(nameRation):
    while True:
        try:
            value = float(input(f"Enter ration {nameRation}: "))
            break
        except ValueError as ex:
            print(ex)
    return value

def findDiskcriminant(a,b,c):
    diskriminant = math.pow(b,2) - 4*a*c
    return diskriminant

def findTheRoots(a,b,disckriminant):
    if(disckriminant>0):
        x1= (-b+math.sqrt(disckriminant))/2/a
        x2=(-b-math.sqrt(disckriminant))/2/a
        print("x1 = ",x1," x2 = ",x2)
    if(disckriminant == 0):
        x=(-b)/2/a
        print("x = ",x)
    if(disckriminant < 0):
        print("no roots")

def main():
    a = enterRationFun("a")
    b = enterRationFun("b")
    c = enterRationFun("c")
    diskcriminant= findDiskcriminant(a,b,c)
    findTheRoots(a,b,diskcriminant)



if __name__=="__main__":
    main()