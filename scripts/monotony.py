from logging import exception
from sympy.parsing.sympy_parser import parse_expr, standard_transformations, implicit_multiplication_application
from sympy import solve


class Monotony():
    def __init__(self):
        self.equation : any
    
    # f'(x) = ?
    def set_function(self, func):
        try:
            transformations = (standard_transformations + (implicit_multiplication_application,))
            equation = parse_expr(func, transformations=transformations)
            self.equation = equation
        except:
            print("FAILED TO PARSE EQUATIONS")


    # f'(x) = 0
    def solve(self):
        result = ""
        try:
            answer = solve(self.equation)
            result += ""
            for r in answer:
                if r == answer[-1]:
                    result += f"x = {r}"
                else:
                    result += f"x = {r}, "
        except:
            result += "FAILED"
        return result

            
    # f'(x) > 0
    def get_greater(self):
        result = ""
        try:
            result += f"{solve(self.equation > 0)}"
        except:
            result += "FAILED"
        return result


    # f'(x) < 0
    def get_smaller(self):
        result = ""
        try:
            result += f"{solve(self.equation < 0)}"
        except:
            result += "FAILED"
        return result