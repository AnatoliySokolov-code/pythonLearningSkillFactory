# Задание 13.5.6
# Запишите логическое выражение, которое определяет,
# что число А не принадлежит интервалу от -10 до -1 или интервалу от 2 до 15.
A = int(input('Введите число: '))
if not (-10 <= A <= -1 or 2 <= A <= 15):
    print("Число не принадлежит интервалу")
else:
    print("Число принадлежит интервалу")
