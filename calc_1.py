import argparse
def calc(num):
    if type(num) is str:
        if num == "ZeroDivisionError" :
            return ("ZeroDivisionError!!! Try again!")
        else:
            return(calc(str_to_list(num)))
    else:
        if len(num) > 1:
            if '*' in num:
                return(mult(num))
            else:
                if '/' in num:
                    return(div(num))
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
        if i.isdigit():
            expr_list += i
        elif i == '-' :
            expr_list += ',' + i + ','
        elif i == '+':
            expr_list += ',' + i + ','
        elif i == '/':
            expr_list += ',' + i + ','
        elif i == '*':
            expr_list += ',' + i + ','
    expr_list = expr_list.split(',')
    return(expr_list)

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

def Main():
    parser = argparse.ArgumentParser()

    parser.add_argument("-cl", "--calculate",action = "store_true")
    parser.add_argument("expression", help = "Expression to calculate", type = str)
    args = parser.parse_args()
    if args.calculate:
        print(calc(args.expression))

if __name__ == '__main__':
    Main()
