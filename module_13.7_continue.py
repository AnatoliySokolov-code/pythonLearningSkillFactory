# Continue
# Если в прошлый раз мы рассмотрели ключевое слово break, которое досрочно
# прерывает выполнение цикла, то сейчас рассмотрим ключевое слово continue.
# Если в теле цикла встречается ключевое слово continue, то цикл пропускает
# весь код до конца тела цикла и переходит на следующий шаг.
#
# Рассмотрим следующую задачу. В клетке находятся фазаны и кролики.
# Известно, что у них 35 голов и 94 ноги. Узнайте число фазанов и число кроликов.
#
# Количество фазанов и кроликов выражается целым числом,
# поэтому будем перебирать все возможные комбинации количества кроликов
# и фазанов, и если суммарное количество их ног равно указанному в условии,
# то мы нашли одно из решений.
heads = 35  # количество голов
legs = 94  # количество ног

for r in range(heads + 1):  # количество кроликов
    for ph in range(heads + 1):  # количество фазанов
        #  если суммарное количество голов превышено или ног превышено, то переходим на следующий шаг цикла
        if (r + ph) > heads or \
                (r * 4 + ph * 2) > legs:
            continue
        if (r + ph) == heads and (r * 4 + ph * 2) == legs:
            print("Количество кроликов", r)
            print("Количество фазанов", ph)
            print("---")
