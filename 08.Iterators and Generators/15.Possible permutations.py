from itertools import permutations


def possible_permutations(data):
    result = permutations(data)
    for info in result:
        yield list(info)


[print(n) for n in possible_permutations([1, 2, 3])]