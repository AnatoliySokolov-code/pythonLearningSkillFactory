# Функция all([ ]) возвращает True, если все элементы списка являются
# истинными. А что если нужно, чтобы был хотя бы один истинный?
# Тогда на помощь приходит функция any([ ]).
# Ее работа аналогична рассмотренному выше примеру.
# Напишите программу, которая на вход принимает последовательность целых чисел,
# и возвращает True, если все числа ненулевые, и False,
# если хотя бы одно число равно 0.
L = list(map(int, input().split()))

print(all(L))