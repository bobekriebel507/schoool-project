import random

def get_random_string(length):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    result = ''
    for i in range(length):
        result += letters[random.randint(0, len(letters) - 1)]
    return result
