# Задание 13.5.9
# Дано натуральное восьмизначное число. Выясните, является ли оно палиндромом
# (читается одинаково слева направо и справа налево).
# Использовать целочисленное деление и деление с остатком не нужно.
# Попробуйте преобразовать число к строке,
# а потом перевернуть эту строку. Смотрите материал прошлого модуля.
num = int(input("Введите натуральное восьмизначное число: "))
print(str(num) == str(num)[::-1])