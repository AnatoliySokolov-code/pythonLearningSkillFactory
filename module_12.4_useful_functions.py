s = "Hello!"
print(len(s))
# 6
print(s.find('e')) # возвращает индекс
# 1

print(s.find('o!')) # в случае подстроки возвращает индекс первого символа
# 4
print(s.find('l')) # встречается в индексах 2 и 3
# 2
print(s.isdigit()) # строка состоит из цифр?
# False

print(s.isalpha()) # строка состоит из букв?
# False

print(s.isalnum()) # строка состоит из цифр и букв?
# False
print(s.upper())
# HELLO!

print(s.lower())
# hello!

print(s)
# Hello!
colors = 'red blue green'
print(colors.split())
# ['red', 'blue', 'green']
path = '/home/user/documents/file.txt'

print(path.split('/')) # разделитель можно указать в качестве аргумента
# ['', 'home', 'user', 'documents', 'file.txt']
colors = 'red green blue'
colors_split = colors.split() # список цветов по отдельности

colors_joined = ' and '.join(colors_split) # объединение строк
print(colors_joined)
# red and green and blue
# Давайте подробнее разберём, что здесь произошло.
# Сначала мы, как и ранее, разбили строку с цветами на несколько подстрок,
# сохранив их в переменную colors_split.
# После чего в переменную colors_joined записали результат объединения строк.
# Чтобы сделать такое преобразование, мы воспользовались методом join().
# Он применяется (через точку, как и все методы) к символу (строке)-разделителю,
# а в аргумент метода помещается список строк, которые нужно объединить.
# В качестве разделителя мы использовали строку and, и Python сам вставил
# её между подстроками с цветами.