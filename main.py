import math


def get_value(nameRation):
    while True:
        try:
            value = float(input(f"Enter ration {nameRation}: "))
            break
        except ValueError as ex:
            print(ex)
    return value


def calculate_diskriminant(a,b,c):
    return math.pow(b,2) - 4*a*c


def calculate_result(a,b,diskriminant):
    result_list=[]
    if(diskriminant>0):
        result_list.append((-b+math.sqrt(diskriminant))/2/a)
        result_list.append((-b-math.sqrt(diskriminant))/2/a)

    if(diskriminant == 0):
        result_list.append((-b)/2/a)

    return result_list

def show_result(result_list):
    if len(result_list) == 0:
        print("no solutions")
    else:
        for i in range(len(result_list)):
            print(f"x{i+1} = {result_list[i]}")


def main():
    a = get_value("a")
    b = get_value("b")
    c = get_value("c")
    diskriminant= calculate_diskriminant(a,b,c)
    show_result(calculate_result(a,b,diskriminant))



if __name__=="__main__":
    main()