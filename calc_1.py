import argparse

from re import findall, fullmatch
from math import radians, sin, cos


SYMBOLS = "1 2 3 4 5 6 7 8 9 0 . ( ) + - * / cos sin"


# Cheking for correct input
def check(expr):
    if fullmatch(r'([0-9()/*\-+.\s]|cos|sin)+', expr):
        return re_magic(expr)
    else:
        return 'Wrong input!!! You may use only {} symbols! Try again!'.format(SYMBOLS)


# Using re lib to make things more easier
def re_magic(expr):
    if 'sin' or 'cos' in expr:
        for i in findall(r'sin\d*|cos\d*',expr):
            trig_to_num = trigonometry(i)
            expr = expr.replace(i, trig_to_num)
    if '(' in expr:
        while '(' in expr:
            for i in findall(r'\([^\(\)]*\)',expr):
                open_par = calc(i)
                expr = expr.replace(i, str(open_par))
        return calc(expr)
    else:
        return calc(expr)


# Calculating all expression
def calc(expr):
    try:
        return float(expr)
    except ValueError:
        if '(' in expr:
            return calc(expr[1:-1])
        for symbol in ['+', '-', '*', '/']:
            if symbol in expr:
                if symbol == '/':
                    symbol_index = expr.rfind(symbol)
                else:
                    symbol_index = expr.find(symbol)
                left_expr = expr[:symbol_index]
                right_expr = expr[symbol_index + 1:]
                return math_action(left_expr, right_expr, symbol)


# Pure math
def math_action(left_expr, right_expr, symbol):
    math_action = {'/': float.__truediv__,
                   '*': float.__mul__,
                   '-': float.__sub__,
                   '+': float.__add__}
    return math_action[symbol](calc(left_expr), calc(right_expr))


# Calculating sin and cos
def trigonometry(expr):
    if expr[:3] == 'sin':
        return str(sin(radians(float(expr[3:]))))
    else:
        return str(cos(radians(float(expr[3:]))))


# Working with a file
def fileoption():
    with open('text.txt') as line:
        num = line.readline().strip()
        b = check(num)
    with open(input("Type here the name of the file:  "), 'a+') as new_line:
        new_line.write(num + '\t')
        new_line.write(b)


# Gives the ability to select the type of input/output
def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("-cl", "--calculate", action='store_true')
    parser.add_argument("-fo", "--fileoption", action='store_true')
    parser.add_argument("-kb", "--keyboard", type = str)
    args = parser.parse_args()
    if args.keyboard:
        print(check(args.keyboard))
    elif args.fileoption:
        fileoption()
        print("New file!!")
    else:
        print(check('1+1'))


if __name__ == '__main__':
    main()
