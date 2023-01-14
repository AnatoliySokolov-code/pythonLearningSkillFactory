a = 3.14
b = '3.14'

print(type(a))
# <class 'float'>
print(type(b))
# <class 'str'>
a = 1
b = 73
c = -12
d = 2
print(type(a))
# <class 'int'>
print(type(b))
# <class 'int'>
print(type(c))
# <class 'int'>
print(type(d))
# <class 'int'>
e = a+b
print(e)
print(type(e))
# 74
# <class 'int'>

f = b*c
print(f)
print(type(f))
# -876
# <class 'int'>

g = b**d # оператор возведения в степень в python обозначается как **
print(g)
print(type(g))
# 5329
# <class 'int'>
x = 0.1
y = 21.5

print(type(x))
# <class 'float'>
print(type(y))
# <class 'float'>
z = y / x
print(z)
print(type(z))
# 215.0
# <class 'float'>