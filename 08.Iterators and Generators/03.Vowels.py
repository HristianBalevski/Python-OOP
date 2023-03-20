class vowels:
    def __init__(self, text):
        self.text = text
        self.vowels = 'AOEIUYaoeiuy'
        self.result = [l for l in reversed(self.text) if l in self.vowels]

    def __iter__(self):
        return self

    def __next__(self):
        while True:
            if not self.result:
                raise StopIteration
            return self.result.pop()


my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)