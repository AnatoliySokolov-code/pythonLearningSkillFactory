# Задание 14.2.2
# Написать функцию, которая будет перемножать любое количество
# переданных ей аргументов.

def multiplication(*nums):
    p = 1
    for n in nums:
        p *= n

    return p

print(multiplication())
print(multiplication(1))
print(multiplication(1, 2))
print(multiplication(1, 2, 3))
