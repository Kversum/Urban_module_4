from math import inf

def divide(first, second):
    """
        Функция должна возвращать результат деления first на second, но когда в second записан 0 - возвращать
        бесконечность.
        Бесконечность можно импортировать из встроенной библиотеки math (from math import inf)
    """
    if second:
        res = first / second
    else:
        res = inf
    return res
