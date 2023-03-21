def get_primes(data):
    for num in data:
        if num >= 2:
            for n in range(2, num):
                if num % n == 0:
                    break
            else:
                yield num


print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))