# Enumerate
# За один проход по циклу for мы можем либо получить само значение из списка,
# либо индекс, по которому дальше можем
# обратиться и получить элемент, к примеру, как здесь:
list_ = [-5, 2, 4, 8, 12, -7, 5]

for i in range(len(list_)):  # равносильно выражению for i in [0, 1, 2, 3, 4, 5, 6]:
    print("Индекс элемента: ", i)
    print("Значение элемента: ", list_[i])  # с помощью индекса получаем значение элемента
    print("---")
print("Конец цикла")
# Но, чтобы убить двух зайцев сразу, есть функция enumerate.
# Она возвращает кортежи,
# где на первом месте стоит индекс элемента, а на втором — его значение.
list_ = [-5, 2, 4, 8, 12, -7, 5]
# Функция enumerate возвращает данные в виде кортежей,
# где на первом месте стоит индекс, а затем значение
# [(0, -5), (1, 2), (2, 4), ...]
for i, value in enumerate(list_):
    print("Индекс элемента: ", i)
    print("Значение элемента: ", value)  # с помощью индекса получаем значение элемента
    print("---")
print("Конец цикла")
# Задание 13.7.1
# Задание на самопроверку.
#
# Начинающий программист написал программу,
# которая находит индекс последнего отрицательного элемента в списке.
list_ = [-5, 2, 4, 8, 12, -7, 5]
# Объявим переменную, в которой будем хранить индекс отрицательного элемента
index_negative = None

for i in range(len(list_)):
    if list_[i] < 0:
        print("Отрицательное число: ", list_[i])
        index_negative = i  # перезаписываем значение индекса
        print("Новый индекс отрицательного числа: ", index_negative)
    else:
        print("Положительное число: ", list_[i])
    print("---")
print("Конец цикла")
print()
print("Ответ: индекс последнего отрицательного элемента = ", index_negative)
# Но он не знал, что есть функция enumerate. Ваша задача — подправить код так,
# чтобы он работал с помощью функции enumerate.
# Решение
list_ = [-5, 2, 4, 8, 12, -7, 5]
# Объявим переменную, в которой будем хранить индекс отрицательного элемента
index_negative = None

for i, value in enumerate(list_):
   if value < 0:
       print("Отрицательное число: ", value)
       index_negative = i  # перезаписываем значение индекса
       print("Новый индекс отрицательного числа: ", index_negative)
   else:
       print("Положительное число: ", value)
   print("---")
print("Конец цикла")
print()
print("Ответ: индекс последнего отрицательного элемента = ", index_negative)