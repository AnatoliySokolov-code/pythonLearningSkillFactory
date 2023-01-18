# Цикл while
# Цикл while подразумевает под собой немного другой подход к ограничению количества шагов, которые должны выполняться. Он выполняется до тех пор, пока истинно его условие. Как только оно становится ложным, цикл прерывается. Для компьютера это выглядит как: «Делай, пока не наступит ...» .
#
# while условие:

    # Начало блока кода с телом цикла
    # пока условие истинно, цикл выполняется
    # ...
    # ...
    # ...
    # Конец блока кода с телом цикла
# Код, который будет выполняться после цикла
# Такой цикл ещё называют циклом с предусловием.
# Давайте разберём работу цикла while на примере.

# Пример 2.
# Условие задачи. Напишите цикл, который будет складывать натуральные числа,
# пока их сумма не превысит 500.
#
# Заранее мы не знаем число шагов нашего цикла, но знаем условие,
# при котором нужно остановиться. Поэтому выбираем цикл while и
# заведем две переменные — для суммы и для текущего числа.

S = 0  # заводим переменную-счетчик, в которой мы будем считать сумму
n = 1  # текущее натуральное число

# заводим цикл while, который будет работать, пока сумма не превысит 500
while S < 500:  # делай пока ...
    S += n  # увеличиваем сумму, равносильно S = S + n
    n += 1  # так как сумма ещё не достигла нужного значения, то увеличиваем переменную-счетчик
    print("Ещё считаю ...")

print("Сумма равна: ", S)
print("Количество чисел: ", n)