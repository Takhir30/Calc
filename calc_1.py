import argparse,math

def calc(num):
    if "sin" in num:
        return(calc(sinus(num)))
    if "cos" in num:
        return(calc(cosinus(num)))
    if type(num) is str:
        if num == "ZeroDivisionError" :
            return ("ZeroDivisionError!!! Try again!")
        else:
            return(calc(str_to_list(num)))
    else:
        if len(num) > 1:

            if '/' in num:
                return(div(num))
            else:
                if '*' in num:
                    return(mult(num))
                else:
                    if '-' in num:
                        return(sub(num))
                    else:
                        if '+' in num:
                            return(add(num))
        else:
            return ("%.2f" % float(num[0]))

def str_to_list(expr_str):
    expr_list = ''
    for i in expr_str:
        if i.isdigit() :
            expr_list += i
        elif i == '-' :
            expr_list += ',' + i + ','
        elif i == '+':
            expr_list += ',' + i + ','
        elif i == '/':
            expr_list += ',' + i + ','
        elif i == '*':
            expr_list += ',' + i + ','
        elif i.isalpha:
            expr_list += i
    expr_list = expr_list.split(',')
    return(expr_list)

def sinus(expr_str):
    b = ''
    for i in expr_str[expr_str.find('sin'):]:
        if i != '-' and i != '+' and i != '/' and i != '*':
            if i.isdigit or i == '.' or i.isalpa:
                b += i
        else: break
    new_expr_str = expr_str.replace('sin' + b[3:],str(round(math.sin(int(b[3:])*math.pi/180),2)))
    return (new_expr_str)

def cosinus(expr_str):
    b = ''
    for i in expr_str[expr_str.find('cos'):]:
        if i != '-' and i != '+' and i != '/' and i != '*':
            if i.isdigit or i == '.' or i.isalpa:
                b += i
        else: break
    new_expr_str = expr_str.replace('cos' + b[3:],str(round(math.sin(int(b[3:])*math.pi/180),2)))
    return (new_expr_str)

def add(expr_list):
    expr_list[expr_list.index('+')-1:expr_list.index('+')+1+1] = [str(float(expr_list[expr_list.index('+')-1]) + float(expr_list[expr_list.index('+')+1]))]
    return (calc(expr_list))

def sub(expr_list):
    expr_list[expr_list.index('-')-1:expr_list.index('-')+1+1] = [str(float(expr_list[expr_list.index('-')-1]) - float(expr_list[expr_list.index('-')+1]))]
    return (calc(expr_list))

def div(expr_list):
    if float(expr_list[expr_list.index('/')+1]) != 0:
        expr_list[expr_list.index('/')-1:expr_list.index('/')+1+1] = [str(float(expr_list[expr_list.index('/')-1]) / float(expr_list[expr_list.index('/')+1]))]
        return (calc(expr_list))
    else:
        return (calc("ZeroDivisionError"))

def mult(expr_list):
    expr_list[expr_list.index('*')-1:expr_list.index('*')+1+1] = [str(float(expr_list[expr_list.index('*')-1]) * float(expr_list[expr_list.index('*')+1]))]
    return (calc(expr_list))

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
