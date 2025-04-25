# calc.py

import argparse

parser = argparse.ArgumentParser(description="CLI Calculator.")

subparser = parser.add_subparsers(help="sub-command help", dest="command")

add = subparser.add_parser("add", help="add integers")
subtract = subparser.add_parser("subtract", help="subtract integers")
multiply = subparser.add_parser("multiply", help="multiply integers")
divide = subparser.add_parser("divide", help="divide integers")

add.add_argument("ints_to_sum", nargs=2, type=int)
subtract.add_argument("ints_to_subtract", nargs=2, type=int)
multiply.add_argument("ints_to_multiply", nargs=2, type=int)
divide.add_argument("ints_to_divide", nargs=2, type=int)

# parser.add_argument("ints_to_sum", nargs=2, type=int)
args = parser.parse_args()
# our_sum = sum(args.ints_to_sum)
# print(f"The sum of values is: {our_sum}")

if args.command == "add":
    our_sum = args.ints_to_sum[0] + args.ints_to_sum[1]
    print(f"The sum of values is: {our_sum}")

elif args.command == "subtract":
    our_sub = args.ints_to_subtract[0] - args.ints_to_subtract[1]
    print(f"The difference of values is: {our_sub}")

elif args.command == "multiply":
    our_m = args.ints_to_multiply[0] * args.ints_to_multiply[1]
    print(f"The multiplication of the values is: {our_m}")

elif args.command == "divide":
    our_d = args.ints_to_divide[0] / args.ints_to_divide[1]
    print(f"The division of the values is: {our_d}")
