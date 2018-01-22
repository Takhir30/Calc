import argparse
import math


symbols = "1234567890.()+-*/"


def check(expr):
    expr = expr.replace(' ', '')    #Removing some extra space's
    for i in ['cos', 'sin']:
        if i in expr:
            new_expr = expr.replace(i, '')
    for i in new_expr:
        if i not in symbols:
            return 'Wrong input!!! You may use only %s symbols! Try again!' % (symbols)
    return calc(expr)


def calc(expr):
    try:
        return  float('%.2f' % float(expr))
    except ValueError:
        for symbol in ['(', '+-', '--', '+', '-', '*-', '/-', '*', '/']:
            if symbol in expr:
                if symbol == '(':
                    return paren(expr)
                else:
                    symbol_index = expr.rfind(symbol)
                    if symbol_index == 0:
                        return calc('0' + expr)
                    left_expr = expr[:symbol_index]
                    right_expr = expr[symbol_index + 1:]
                    return math_action(left_expr, right_expr, symbol[0])
        if 'sin' in expr or 'cos' in expr:
                return calc(trigonometry(expr))


def paren(expr):        #parenthesis
    i_index = 0
    for i in expr:
        if i == '(':
            left_index = i_index
        if i == ')':
            right_index = i_index
            break
        i_index += 1
    new_expr = expr.replace(expr[left_index:right_index + 1], str(calc(expr[left_index + 1:right_index])))
    return calc(new_expr)


def math_action(left_expr, right_expr, symbol):
    math_action = {'/': float.__truediv__,
                   '*': float.__mul__,
                   '-': float.__sub__,
                   '+': float.__add__}
    return math_action[symbol](calc(left_expr), calc(right_expr))


def trigonometry(expr):
    rad_to_degree = float(expr[3:]) * math.pi / 180
    if expr[:3] == 'sin':
        return math.sin(rad_to_degree)
    else:
        return math.cos(rad_to_degree)


def fileoption():
    with open('text.txt') as line:
        num = line.readline().strip()
        b = check(num)
    with open(input("Type here the name of the file:  "), 'a+') as new_line:
        new_line.write(num + '\t')
        new_line.write(b)


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("-cl", "--calculate" , action='store_true')
    parser.add_argument("-fo", "--fileoption" , action='store_true')
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
