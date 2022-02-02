from cmath import sqrt
from math import sqrt

def distinctive(a, b, c):
    a = int(a)
    b = int(b)
    c = int(c)
    
    d = b**2 -4*a*c
    
    result = ""
    if d > 0:
        x1 = (-b - sqrt(d))/(2*a)
        x2 = (-b + sqrt(d))/(2*a)
        
        if x1 == int(x1):
            result += f"{int(x1)}, "
        else:
            result += f"{format(x1, '.2f')}, "
            
        if x2 == int(x2):
            result += f"{int(x2)}"
        else:
            result += f"{format(x2, '.2f')}"
            
    elif d == 0:
        x = (-b)/(2*a)
        
        if x == int(x):
            result += f"{int(x)}"
        else:    
            result += f"{format(x, '.2f')}"
    else:
        result = "impossible"
    
    return result