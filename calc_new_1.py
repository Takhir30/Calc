import argparse
import numexpr as ne


def Main():
    parser = argparse.ArgumentParser()

    parser.add_argument("-cl", "--calculate", help = "Expression to calculate", type = str)
    args = parser.parse_args()
    if args.calculate:
        print(ne.evaluate(args.calculate))

if __name__ == '__main__':
    Main()
