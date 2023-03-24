def cache(func):
    memo = {}

    def wrapper(number):
        if number in memo:
            return memo[number]
        result = (func(number))
        memo[number] = result

        return result

    wrapper.log = memo
    return wrapper


@cache
def fibonacci(n):
    if n < 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


fibonacci(5)
print(fibonacci.log)