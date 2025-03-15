import random

def get_random_number(minimum, maximum):
    return random.randint(minimum, maximum)

if __name__ == "__main__":
    minimum = 1
    maximum = 10
    print(get_random_number(minimum, maximum))
