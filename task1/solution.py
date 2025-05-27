import inspect


def strict(func):
    signature = inspect.signature(func)

    def wrapper(*args, **kwargs):
        arguments = signature.bind(*args, **kwargs).arguments

        for argument_name, argument_value in arguments.items():
            expected_type = signature.parameters[argument_name].annotation
            if expected_type != type(argument_value):
                raise TypeError(
                    f'Аргумент "{argument_name}" '
                    f'не соответствует типу данных {expected_type.__name__}'
                )
        return func(*args, **kwargs)
    return wrapper


@strict
def sum_two(a: int, b: int) -> int:
    return a + b
