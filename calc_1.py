import argparse
import math


def calc(expr):

    math_action = {'sin':sinus, "cos":cosinus, '/':div,
                   '*':mult, '-':sub, '+':add}
    if len(expr) > 1:
        for i in ['sin','cos','/','*','-','+']:
            if type(expr) is str:
                if i in expr and i not in '/*-+':
                    return math_action[i](expr)
                if expr == "ZeroDivisionError" :
                    return ("ZeroDivisionError!!! Try again!")
                else:
                    return str_to_list(expr)
            else:
                if i in expr:
                    return math_action[i](expr)
    else:
        return ("%.2f" % float(expr[0]))


def str_to_list(expr_str):
    expr_list = ''
    for i in expr_str:
        if i in '+/*-' :
            expr_list += ',' + i + ','
        else:
            expr_list += i
    expr_list = expr_list.split(',')
    return calc(expr_list)


def sinus(expr_str):
    b = ''
    for i in expr_str[expr_str.find('sin'):]:
        if i not in '+-/*':
            if i.isdigit or i == '.' or i.isalpa:
                b += i
        else:
            break
    new_expr_str = expr_str.replace('sin' + b[3:], str(round(math.sin(int(b[3:]) * math.pi/180), 2)))
    return calc(new_expr_str)


def cosinus(expr_str):
    b = ''
    for i in expr_str[expr_str.find('cos'):]:
        if i not in '+-/*':
            if i.isdigit or i == '.' or i.isalpa:
                b += i
        else:
            break
    new_expr_str = expr_str.replace('cos' + b[3:], str(round(math.sin(int(b[3:]) * math.pi / 180), 2)))
    return calc(new_expr_str)


def add(expr_list):
    plus = expr_list.index('+')
    expr_list[plus - 1:plus + 2] = [str(float(expr_list[plus - 1]) + float(expr_list[plus + 1]))]
    return calc(expr_list)


def sub(expr_list):
    minus = expr_list.index('-')
    expr_list[minus - 1:minus + 2] = [str(float(expr_list[minus - 1]) - float(expr_list[minus + 1]))]
    return (calc(expr_list))


def div(expr_list):
    slash = expr_list.index('/')
    if float(expr_list[slash + 1]) != 0:
        expr_list[slash - 1:slash + 2] = [str(float(expr_list[slash - 1]) / float(expr_list[slash + 1]))]
        return calc(expr_list)
    else:
        return calc("ZeroDivisionError")


def mult(expr_list):
    star = expr_list.index('*')
    expr_list[star - 1:star + 2] = [str(float(expr_list[star - 1]) * float(expr_list[star + 1]))]
    return calc(expr_list)


def fileoption():
    with open('text.txt') as line:
        num = line.readline().strip()
        b = calc(num)
    with open(input(),'a+') as new_line:
        new_line.write(num + '\t')
        new_line.write(b)


def Main():
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
    Main()
