def divide(first, second):
    """
    Функция должна возвращать результат деления first на second, но когда в second записан 0 - возвращать
    строку 'Ошибка'.
    """
    if second:
        res = first / second
    else:
        res = 'Ошибка, делить на ноль нельзя.'
    return res


