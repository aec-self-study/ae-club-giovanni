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

args = parser.parse_args()

if args.command == "add":
    our_sum = sum(args.ints_to_sum)
    print(f"The sum of values is: {our_sum}")

elif args.command == "subtract":
    if not args.ints_to_subtract:
        print("Please provide at least one number to subtract")
    else:
        result = args.ints_to_subtract[0]
        for num in args.ints_to_subtract[1:]:
            result -= num
        print(f"The difference of values is: {result}")

elif args.command == "multiply":
    result = 1
    for num in args.ints_to_multiply:
        result *= num
    print(f"The product of values is: {result}")

elif args.command == "divide":
    if args.ints_to_divide[1] == 0:
        print("cannot divide by zero")
    else:
        result = args.ints_to_divide[0] / args.ints_to_divide[1]
        print(f"The division result is: {result}")
