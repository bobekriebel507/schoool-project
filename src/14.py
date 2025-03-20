def calculate_average(numbers):
    total = sum(numbers)
    average = total / len(numbers)
    return average

if __name__ == "__main__":
    numbers = [10, 20, 30, 40, 50]
    print("The average is:", calculate_average(numbers))
