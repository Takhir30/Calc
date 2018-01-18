import argparse
import math


def calc(expr):
    try:
        num = float(expr)
        return  num
    except ValueError:
        for symbol in ['+', '-', '*', '/']:
            if symbol in expr:
                symbol_index = expr.find(symbol)
                left_expr = expr[:symbol_index]
                right_expr = expr[symbol_index+1:]
                return math_action(left_expr, right_expr, symbol)
        if 'sin' in expr or 'cos' in expr:
                return calc(trigonometry(expr))


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
        b = calc(num)
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
        print(calc(args.keyboard))
    elif args.fileoption:
        fileoption()
        print("New file!!")
    else:
        print(calc('1+1'))


if __name__ == '__main__':
    main()
