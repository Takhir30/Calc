import argparse
import math
import re


symbols = "1234567890.()+-*/"


# Cheking for correct input
def check(expr):
    if re.fullmatch(r'([0-9()/*\-+.\s]|cos|sin)+', expr):
        return str_to_list(expr)
    else:
        return 'Wrong input!!! You may use only %s symbols! Try again!' % (symbols)


# Turning our expression from string to list
def str_to_list(expr_str):
    expr_list = ''
    for i in expr_str:
        if i in '+-*/()' :
            expr_list += ',' + i + ','
        else:
            expr_list += i
    expr_list = expr_list.replace(',,', ',').split(',')
    expr_list = list(filter(lambda x: x, expr_list))
    return calc(expr_list)


# Calculating all expression
def calc(expr):
    if expr[0] == '-':
        expr[0:2] = ['-' + expr[1]]
    if len(expr) == 1:
        try:
            return float('%.2f' % float(expr[0]))
        except ValueError:
            return trigonometry(expr)
    else:
        if '(' in expr:
            return paren(expr)
        for symbol in ['+', '-', '*', '/']:
            if symbol in expr:
                symbol_index = -1
                for i in expr[-1::-1]:
                    if i == symbol:
                        break
                    symbol_index -= 1
                left_expr = expr[:symbol_index]
                right_expr = expr[symbol_index + 1:]
                return math_action(left_expr, right_expr, symbol)


# Calculating expression in parenthesis
def paren(expr):       
    i_index = 0
    for i in expr:
        if i == '(':
            left_index = i_index
        if i == ')':
            right_index = i_index
            break
        i_index += 1
    expr[left_index:right_index + 1] = [calc(expr[left_index + 1:right_index])]
    return calc(expr)


# Pure math
def math_action(left_expr, right_expr, symbol):
    math_action = {'/': float.__truediv__,
                   '*': float.__mul__,
                   '-': float.__sub__,
                   '+': float.__add__}
    return math_action[symbol](calc(left_expr), calc(right_expr))


# Calculating sin and cos
def trigonometry(expr):
    rad_to_degree = float(expr[0][3:]) * math.pi / 180
    if expr[0][:3] == 'sin':
        return calc([math.sin(rad_to_degree)])
    else:
        return calc([math.sin(rad_to_degree)])


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
