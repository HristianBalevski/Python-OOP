def type_check(type_obj):
    def decorator(func_ref):
        def wrapper(argument):
            if not isinstance(argument, type_obj):
                return 'Bad Type'
            return func_ref(argument)

        return wrapper

    return decorator


@type_check(int)
def times2(num):
    return num*2


print(times2(2))
print(times2('Not A Number'))