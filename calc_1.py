def str_to_list(expr_str):
    expr_list = ''
    for i in expr_str:
        if i.isdigit():
            expr_list += i
        elif i == '-' :
            expr_list += ',' + i + ','
        elif i == '+':
            expr_list += ',' + i + ','
    expr_list = expr_list.split(',')
    return(expr_list)

def add(expr_list):
    expr_list[expr_list.index('+')-1:expr_list.index('+')+1+1] = [str(float(expr_list[expr_list.index('+')-1]) + float(expr_list[expr_list.index('+')+1]))]
    return (calc(expr_list))

def sub(expr_list):
    expr_list[expr_list.index('-')-1:expr_list.index('-')+1+1] = [str(float(expr_list[expr_list.index('-')-1]) - float(expr_list[expr_list.index('-')+1]))]
    return (calc(expr_list))


def calc(num):
    if type(num) is str:
        return(calc(str_to_list(num)))
    else:
        if len(num) > 1:
            if '-' in num:
                return(sub(num))
            else:
                if '+' in num:
                    return(add(num))
        else:
            return (float(num[0]))

def Main():
    print(calc('2+3+1-9'))

if __name__ == '__main__':
    Main()
