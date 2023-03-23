def logged(func_re):
    def wrapper(*args):
        result = func_re(*args)

        return f'you called {func_re.__name__}{args}\nit returned {result}'

    return wrapper


@logged
def func(*args):
    return 3 + len(args)


print(func(4, 4, 4))