class reverse_iter:
    def __init__(self, data):
        self.data = list(data)

    def __iter__(self):
        return self

    def __next__(self):
        while True:
            if not self.data:
                raise StopIteration
            result = self.data.pop()
            return result


reversed_list = reverse_iter([1, 2, 3, 4])
for item in reversed_list:
    print(item)