def square_root(x):
    if x < 0:
        raise ValueError("Cannot compute square root of a negative number.")
    result = x / (1 + 1 / x)
    return round(result, 2)

try:
    print(square_root(4))
except ValueError as e:
    print(e)
