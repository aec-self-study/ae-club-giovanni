import argparse

parser = argparse.ArgumentParser(description="CLI Calculator.")

subparser = parser.add_subparsers(help="sub-command help", dest="command")

add = subparser.add_parser("add", help="add integers")
subtract = subparser.add_parser("subtract", help="subtract integers")
multiply = subparser.add_parser("multiply", help="multiply integers")
divide = subparser.add_parser("divide", help="divide integers")

add.add_argument("ints_to_sum", nargs='*', type=int, help="integers to sum")
subtract.add_argument("ints_to_subtract", nargs='*', type=int,
                      help="first number minus all subsequent numbers")
multiply.add_argument("ints_to_multiply", nargs='*',
                      type=int, help="integers to multiply")
divide.add_argument("ints_to_divide", nargs=2, type=int,
                    help="two integers to divide (numerator denominator)")


def aec_subtract(ints_to_sub):
    result = ints_to_sub[0]
    for num in ints_to_sub[1:]:
        result -= num
    if result < 0:
        result = 0
    print(f"The difference of values is: {result}")
    return result


def aec_divide(ints_to_div):
    if len(ints_to_div) > 2:
        raise Exception("more than two args")
    if ints_to_div[1] == 0:
        print("cannot divide by zero")
        return (0)
    else:
        result = ints_to_div[0] / ints_to_div[1]
        print(f"The division result is: {result}")
        return result


if __name__ == "__main__":
    args = parser.parse_args()

    if args.command == "add":
        our_sum = sum(args.ints_to_sum)
        print(f"The sum of values is: {our_sum}")

    elif args.command == "subtract":
        if not args.ints_to_subtract:
            print("Please provide at least one number to subtract")
        else:
            aec_subtract(args.ints_to_subtract)

    elif args.command == "multiply":
        result = 1
        for num in args.ints_to_multiply:
            result *= num
        print(f"The product of values is: {result}")

    elif args.command == "divide":
        aec_divide(args.ints_to_divide)
