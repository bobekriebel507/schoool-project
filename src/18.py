import math
import random

def generate_random_number():
    """
    Generate a random number between 0 and 1.
    """
    return random.random()

def generate_random_float():
    """
    Generate a random floating point number between 0.0 and 1.0.
    """
    return random.uniform(0, 1)

def generate_random_string(length=8):
    """
    Generate a random string of given length.
    """
    return ''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(length))

def main():
    print("Random number: ", generate_random_number())
    print("Random float: ", generate_random_float())
    print("Random string: ", generate_random_string())

if __name__ == "__main__":
    main()
