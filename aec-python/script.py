# Variables and Calculations
x = 2

print(x)

print(x**2)

y = "hello"
print(y)

z = x**2 + 5*x
print(z)


# Lists
my_list = ['apple', 1, 'banana', 2, 3, 'oranges', 3.5]

my_list

my_fruit_list = ['apple', 'banana']
my_int_list = [1, 2, 3]

my_fruit_list[1]
my_fruit_list[0]

# Dictionaries
cal_lookup = {'apple': 95, 'banana': 105, 'orange': 45}

cal_lookup['apple']

# Loops

for f in my_fruit_list:
    print(f)

for i in my_int_list:
    print(i)

for i in my_int_list:
    pass
print(i)  # Will output only the last i value, so in this case 3

# Functions


def sq_int(x):
    y = x**2
    return y


sq_int(5)

# Conditional Flow

x = 5
y = 4


# Read about:
# while
# pass

# Write a loop that uses while instead of the built-in looping structure.
i = 1
while i < 6:
    print(i)
    i += 1

# Write a loop that loops over the keys in a dictionary and prints the values.
cal_lookup = {'apple': 95, 'banana': 105, 'orange': 45}
print(len(cal_lookup))

for n in cal_lookup:
    print(n)
    print(cal_lookup[n])

for item in cal_lookup.keys():
    print(cal_lookup[item])

# Write the functions is_odd and is_even that are shown in the lecture.


def is_even(num):
    return (num % 2 == 0)


is_even(2)


def is_odd(num):
    return (num % 2 != 0)


is_odd(2)

# Loop over my_first_list and square the value if the value is a number, and print the calories of the fruit if it’s a fruit (hint: use the dictionary to look up the calories).
for n in my_list:
    if type(n) == int or type(n) == float:
        print(n**2)
    else:
        pass

# Write a function that:
# Takes a dictionary as an argument.
# Loops over the keys in the dictionary.
# Prints the square of the value in the value.
# Hint: use the cal_lookup dictionary for testing.


def ourfun(dict):
    for k in dict.keys():
        print(dict[k]**2)


ourfun(cal_lookup)

#####


def describe_eveness(x):
    if is_even(x):
        print("It's even!")
    elif is_odd(x):
        print("It's odd!")
    else:
        print("It's neither even nor odd!")


describe_eveness(x)

describe_eveness(y)
