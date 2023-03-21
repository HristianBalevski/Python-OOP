class dictionary_iter:
    def __init__(self, dict_object):
        self.dict_object = list(dict_object.items())
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count == len(self.dict_object):
            raise StopIteration
        output = self.dict_object[self.count]
        self.count += 1
        return output


result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(tuple(x))

