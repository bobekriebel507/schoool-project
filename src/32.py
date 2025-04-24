class MyClass:
    def __init__(self):
        self.data = []

    def add_data(self, item):
        self.data.append(item)

    def get_data(self):
        if len(self.data) == 0:
            raise ValueError("Data is empty")
        return self.data[0]

# Example usage
data = MyClass()
data.add_data(1)
print(data.get_data())  # Output: 1
