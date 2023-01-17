x = float(input("Введите  число Х не равное 0: "))
y = float(input("Dведите  число Y не равное 0: "))
if x > 0 and y > 0:
    print("Первая четверть")
if x > 0 and y < 0:
    print("Четвертая четверть")
if x < 0 and y > 0:
    print("Вторая четверть")
if x < 0 and y < 0:
    print("Третья четверть")