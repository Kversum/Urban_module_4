"""
Пункты задачи:
Создайте модули fake_math и true_math.
Напишите функции divide в обоих методах. Разница между этими функциями - возвращаемое значение.
Создайте модуль module_4_1 (если ещё не создан), импортируйте в него функции divide из модулей fake_math и true_math,
назвав их разными именами на своё усмотрение, чтобы не было конфликтов имён, при помощи оператора as.
Запустите эти функции в модуле module_4_1, передав первым аргументом произвольное число отличное от 0,
вторым аргументом - 0
Выведи результаты вызовов этих функций на экран(в консоль).
"""
import fake_math as divide_fm
import true_math as divide_tm

result1 = divide_fm.divide(69, 3)
result2 = divide_fm.divide(3, 0)
result3 = divide_tm.divide(49, 7)
result4 = divide_tm.divide(15, 0)
print(result1)
print(result2)
print(result3)
print(result4)