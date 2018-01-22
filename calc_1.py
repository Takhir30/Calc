import argparse
import math


symbols = "1234567890.()+-*/"


def check(expr):
    expr = expr.replace(' ', '')    #Removing some extra space's
    for i in ['cos', 'sin']:
        if i in expr:
            new_expr = expr.replace(i, '')
        else:
            new_expr = expr
    for i in new_expr:
        if i not in symbols:
            return 'Wrong input!!! You may use only %s symbols! Try again!' % (symbols)
    return str_to_list(expr)



def str_to_list(expr_str):
    if 'sin' in expr_str or 'cos' in expr_str:
            return trigonometry(expr_str)
    expr_list = ''
    for i in expr_str:
        if i.isdigit() or i == '.':
            expr_list += i
        elif i in '+-*/()' :
            expr_list += ',' + i + ','
    expr_list = expr_list.replace(',,',',').split(',')
    expr_list = [x for x in expr_list if x]
    return calc(expr_list)


def calc(expr):
    if expr[0] == '-':
        expr[0:2] = ['-' + expr[1]]
    if len(expr) == 1:
        return  float('%.2f' % float(expr[0]))
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



def paren(expr):        #parenthesis
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


def math_action(left_expr, right_expr, symbol):
    math_action = {'/': float.__truediv__,
                   '*': float.__mul__,
                   '-': float.__sub__,
                   '+': float.__add__}
    return math_action[symbol](calc(left_expr), calc(right_expr))


def trigonometry(expr):
    rad = ''
    for i in ['sin', 'cos']:
        if i in expr:
            tr_l_index = expr.find(i)
            for j in expr[tr_l_index + 3:]:
                if j.isdigit() or j == '.':
                    rad += j
                else:
                    break
        rad_to_degree = float(rad) * math.pi / 180
        tr_r_index = tr_l_index + 3 + len(rad)
        if i == 'sin':
            expr = expr.replace(expr[tr_l_index:tr_r_index], str(math.sin(rad_to_degree)))
        else:
            expr = expr.replace(expr[tr_l_index:tr_r_index], str(math.cos(rad_to_degree)))
        return str_to_list(expr)


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
