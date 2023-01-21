# Задание 14.2.1
# Подумайте, что будет выведено в результате выполнения данной программы?
x = 3
def function():
    print(x)
    return x

print(function())

x = 3


def func():
   global x # объявляем, что переменная является глобальной
   print(x)
   x = 5
   x += 5
   return x


func()
print(x)
