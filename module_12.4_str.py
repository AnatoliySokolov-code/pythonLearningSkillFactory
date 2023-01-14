s1 = 'hello' # используя апострофы
s2 = "hola" # используя кавычки
s3 = '''Привет!
        Хорошего дня!''' # используя тройные "апострофы" или тройные кавычки
s = "Hello!"

print(s[0])
# H

print(s[4])
# o
print(s[1:4])
# ell
print(s[2:])
# llo!
print(s[:4])
# Hell
print(s[::2])
# Hlo
print(s[::-1])
# !olleH
print(s[-1])
# !

print(s[-3:-1])
# lo