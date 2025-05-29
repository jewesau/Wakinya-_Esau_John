from multipledispatch import dispatch

# Multiply two integers
@dispatch(int, int)
def multiply(a, b):
    return a * b

# Multiply two floats
@dispatch(float, float)
def multiply(a, b):
    return round(a * b, 2)

# Multiply int and float
@dispatch(int, float)
def multiply(a, b):
    return round(a * b, 2)

# Multiply float and int
@dispatch(float, int)
def multiply(a, b):
    return round(a * b, 2)

# Test the overloaded multiply function
print(multiply(3, 4))        # 12 (int * int)
print(multiply(3.5, 2.0))    # 7.0 (float * float)
print(multiply(3, 2.5))      # 7.5 (int * float)
print(multiply(2.5, 3))      # 7.5 (float * int)
