numbers = input("Введите последовательность чисел через пробел: ").split()
target = int(input("Введите любое число: "))
# преобразуем последовательность в список
numbers_list = [int(num) for num in numbers]
# проверяем, есть ли число target в списке
if target in numbers_list:
    print("Число", target, "найдено в списке")

# Функция сортировки списка
def sort_list(numbers_list):
    for i in range(len(numbers_list)):
        for j in range(i + 1, len(numbers_list)):
            if numbers_list[i] > numbers_list[j]:
                numbers_list[i], numbers_list[j] = numbers_list[j], numbers_list[i]
    return numbers_list

# Вызываем функцию сортировки списка
print("Отсортированный по возрастанию список: ", sort_list(numbers_list))
# Функция двоичного поиска
def binary_search(numbers_list, target):
    low = 0
    high = len(numbers_list) - 1
    while low <= high:
        mid = (low + high) // 2
        if target == numbers_list[mid]:
            return mid
        elif target < numbers_list[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return low

# Вызываем функцию двоичного поиска
position = binary_search(numbers_list, target)

# Выводим результат
if position < len(numbers_list):
    print("Номер позиции элемента, который меньше введенного пользователем числа:", position)
else:
    print("Введенное число больше всех элементов списка")