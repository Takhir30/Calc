import argparse
import math


def calc(expr):
    try:
        math_action = {'sin': trigonometry,
                       'cos': trigonometry,
                       '/': div,
                       '*': mult,
                       '-': sub,
                       '+': add}
        for i in ['sin', 'cos', '/', '*', '-', '+']:
            if i in expr:
                return math_action[i](i,expr)
        return "%.2f" % float(expr)
    except ZeroDivisionError:
        print("Division by zero!")


def a_num(sign, expr):
    a = ''
    a_index = expr.find(sign)
    for i in expr[a_index-1::-1]:
        if i.isdigit() or i == '.':
            a += i
            a_index -= 1
        else:
            break
    return float(a[::-1]), a_index


def b_num(sign, expr):
    b = ''
    b_index = expr.find(sign)
    for i in expr[b_index + 1:]:
        if i.isdigit() or i == '.':
            b += i
            b_index += 1
        else:
            break
    return float(b), b_index + 1


def data_num(sign,expr):
    a, a_index = a_num(sign, expr)
    b, b_index = b_num(sign, expr)
    return a, a_index, b, b_index


def trigonometry(tr_sign, expr):
    b = ''
    for i in expr[expr.find(tr_sign):]:
        if i not in '+-/*':
            if i.isdigit() or i == '.' or i.isalpa():
                b += i
        else:
            break
    trig = tr_sign + b[3:]
    rad_to_degree = int(b[3:]) * math.pi/180
    if tr_sign == 'sin':
        new_expr = expr.replace(trig, str(math.sin(rad_to_degree)))
    else:
        new_expr = expr.replace(trig, str(math.cos(rad_to_degree)))
    return calc(new_expr)


def add(sign,expr):
    a, a_index, b, b_index = data_num(sign,expr)
    new_expr = expr.replace(expr[a_index:b_index],str(a+b))
    return calc(new_expr)


def sub(sign,expr):
    a, a_index, b, b_index = data_num(sign,expr)
    new_expr = expr.replace(expr[a_index:b_index],str(a-b))
    return calc(new_expr)


def div(sign,expr):
    a, a_index, b, b_index = data_num(sign,expr)
    new_expr = expr.replace(expr[a_index:b_index],str(a/b))
    return calc(new_expr)


def mult(sign,expr):
    a, a_index, b, b_index = data_num(sign, expr)
    new_expr = expr.replace(expr[a_index:b_index],str(a*b))
    return calc(new_expr)


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
