from random import randint

def generate_random_python_code():
    lines = []
    for i in range(randint(1, 5)):
        line = f"print('Hello, world!')\n"
        lines.append(line)
    return "".join(lines)