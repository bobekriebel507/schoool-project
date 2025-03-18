 import random
def get_random_code():
    numbers = "1234567890"
    lowercase = "abcdefghijklmnopqrstuvwxyz"
    uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    symbols = "!@#$%^&*()-_=+[]{};:'\"<>,./?|"
    all_characters = numbers + lowercase + uppercase + symbols
    random_code = ""
    for i in range(8):
        random_code += random.choice(all_characters)
    return random_code