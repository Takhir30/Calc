import argparse
import numexpr as ne

def fileoption():
    with open('text.txt') as line:
        num = line.readline().strip()
        b = ne.evaluate(num)
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
        print(ne.evaluate(args.keyboard))
    elif args.fileoption:
        fileoption()
        print("New file!!")
    else:
        print(ne.evaluate('1+1'))

if __name__ == '__main__':
    Main()
