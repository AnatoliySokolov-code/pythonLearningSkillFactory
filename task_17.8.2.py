array = [2, 3, 1, 4, 6, 5, 9, 8, 7]


count = 0
for i in range(len(array)):  # проходим по всему массиву
    idx_min = i  # сохраняем индекс предположительно минимального элемента
    for j in range(i, len(array)): #   или чтобы отказаться от этой проверки можно заменить эту строку на for j in range(i+1, Len(array)):
        count += 1
        if array[j] < array[idx_min]:
            idx_min = j
        # count += 1 в этой строчке уберите отступ (выведите из цикла), если вы хотите считатьсравнения индекса с минмимальным , или уберите строку совсем, если требуются только чистые сравнения, т.е.чисел массива между собой.
    if i != idx_min:  # если индекс не совпадает с минимальным, меняем
        array[i], array[idx_min] = array[idx_min], array[i]

print('Compares: ', count)