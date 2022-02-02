from sympy import re

def power_3(fx3, fx2, fx1, fx0):
    r_list = []
    
    f1 = int(fx3)
    f2 = int(fx2)
    f3 = int(fx1) 
    f4 = int(fx0)
    if f4 < 0:
        f = f4 * -1
    else:
        f = f4

    for i in range(f * -1, f + 1):
        if i != 0:
            if f4 % i == 0:
                r = i
                seq = f4 - (f3 - (f2 - (f1 * r)) * r) * r
                if seq == 0:
                    r_list.append(r * -1)
    if len(r_list) > 0:
        return min(r_list)
    else:
        return "None"

    for i in r_list:
        if i != r_list[-1]:
            print(i, end=", ")
        else:
            print(i)
            
def power_4(fx4, fx3, fx2, fx1, fx0):
    r_list = []
    
    f1 = int(fx4)
    f2 = int(fx3)
    f3 = int(fx2)
    f4 = int(fx1) 
    f5 = int(fx0)
    if f5 < 0:
        f = f5 * -1
    else:
        f = f5

    for i in range(f * -1, f + 1):
        if i != 0:
            if f5 % i == 0:
                r = i
                seq = f5 - (f4 - (f3 - (f2 - (f1 * r)) * r) * r) * r
                if seq == 0:
                    r_list.append(r * -1)
                    
    if len(r_list) > 0:
        result = ""
        r_list.sort()
        for r in r_list:
            if r != r_list[-1]:
                result += f"{r}, "
            else:
                result += f"{r}"
        return result
    else:
        return "None"
    
    for i in r_list:
        if i != r_list[-1]:
            print(i, end=", ")
        else:
            print(i)