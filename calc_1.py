import argparse
import math


def calc(expr):
    for i in ['sin', 'cos', '/', '*', '-', '+']:
        if i in expr:
            return action(i, expr)
    return "%.2f" % float(expr)


def left_num(sign, expr):
    a = ''
    a_index = expr.find(sign)
    for i in expr[a_index-1::-1]:
        if i.isdigit() or i == '.':
            a += i
            a_index -= 1
        else:
            break
    return float(a[::-1]), a_index


def right_num(sign, expr):
    b = ''
    b_index = expr.find(sign)
    for i in expr[b_index + 1:]:
        if i.isdigit() or i == '.':
            b += i
            b_index += 1
        else:
            break
    return float(b), b_index + 1


def action(sign, expr):
    math_action = {'sin': trigonometry,
                   'cos': trigonometry,
                   '/': div,
                   '*': mult,
                   '-': sub,
                   '+': add}
    if sign in '/*-+':
        a, a_index = left_num(sign, expr)
        b, b_index = right_num(sign, expr)
        new_expr = expr.replace(expr[a_index:b_index], math_action[sign](a, b))
        return calc(new_expr)
    else:
        trigonometry(sign, expr)


def trigonometry(tr_sign, expr):
    b = ''
    trig_index = expr.find(tr_sign) + 3
    for i in expr[trig_index:]:
        if i.isdigit() or i == '.':
            b += i
    trig = sign + b
    rad_to_degree = int(b) * math.pi / 180
    if tr_sign == 'sin':
        new_expr = expr.replace(trig, str(math.sin(rad_to_degree)))
    else:
        new_expr = expr.replace(trig, str(math.cos(rad_to_degree)))
    return calc(new_expr)


def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mult(a, b):
    return a * b


def div(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return("ZeroDivisionError")


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
