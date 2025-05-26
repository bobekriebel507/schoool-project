import random
import time

def fetch_random_data():
    data = ["data1", "data2", "data3"]
    return random.choice(data)

while True:
    print(fetch_random_data())
    time.sleep(60)
