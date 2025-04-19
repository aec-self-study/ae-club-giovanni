import random

denoms = list(range(10))
print(denoms)

random.shuffle(denoms)

# 1. Use prints to understand better what is failing

for i in range(10):
    print(f'i: {i}')
    x = denoms[i]
    print(f'x: {x}')
    result = 100 / x

# 2. Use Debugger!

for i in range(10):
    import pdb
    pdb.set_trace()
    x = denoms[i]
    result = 100 / x

# import pdb - python debugger
# pdb.set_trace() --> very useful command to trace error in your code (?)
# l - list where you are in the code, which line.
# you can write any variable and it will output it --> in our case x, or i, or result,
# n - next line, or again at the top of the loop!
# c - continue
# q - quit the debugger

# 3. Try - Except Patterns

for i in range(10):
    x = denoms[i]
    try:
        result = 100 / x
    except:
        print("something is wrong")
        import pdb
        pdb.set_trace()
