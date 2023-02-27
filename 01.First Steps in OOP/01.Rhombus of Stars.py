size = int(input())

for x in range(size):
    space = size - x - 1
    stars = x + 1
    print(' ' * space + '* ' * stars)

for x in range(size - 2, -1, -1):
    space = size - x - 1
    stars = x + 1
    print(' ' * space + '* ' * stars)
