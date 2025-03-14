import random

def get_random_word():
    with open('words.txt') as f:
        words = f.read().splitlines()
    return random.choice(words)