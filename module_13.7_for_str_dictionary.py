# Цикл for со строками и словарями
# Цикл for может работать не только со списками, но и со строками и словарями.
# Давайте рассмотрим задачу для подсчета количества символов в тексте.
# Условие задачи: С помощью словаря в заданном тексте посчитать количество
# вхождения каждого символа.
text = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо -- песнь заводит,
Налево -- сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух... там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""

text = text.lower()
text = text.replace(" ", "")
text = text.replace("\n", "")
print(text)
# Символы в верхнем и нижнем регистре будем считать одинаковыми,
# поэтому приведем текст в нижний регистр. И удалим все пробелы и символы
# переноса строки.
count = {}  # для подсчета символов и их количества
for char in text:
   if char in count:  # если символ уже встречался, то увеличиваем его количество на 1
       count[char] += 1
   else:
       count[char] = 1
# Заводим переменную «счетчик» в виде словаря, где по ключу будет храниться
# символ, по значению — его количество. Далее с помощью цикла for
# посимвольно будем проходиться по обработанному тексту и считать символы.
for char, cnt in count.items():
   print(f"Символ {char} встречается {cnt} раз")
# После подсчета применим цикл for для работы со словарем.
# У словаря есть метод items, который возвращает кортежи состоящие
# из пар ключ-значение. Зная их, можно вывести статистику по тексту.
#
# f-строки делают форматирование более удобным и позволяют писать переменные
# в фигурных скобках по мере их использования в тексте.
# Метод доступен, начиная с версии Python 3.6, и значительно упрощает
# синтаксис работы со строками.
# Приведем примеры:
# 1.Обычная строка:  print("Меня зовут " + name + ". Мне " + str(age) + " лет.")
# 2.Строка с форматированием %: print("Меня зовут %(name)s. Мне %(age)d лет." % {"name": name, "age": age})
# 3.Использование f-строк последней версии: print(f"Меня зовут {name} Мне {age} лет.")
# Видно, что для использования необходимо поставить f перед строкой и
# добавить переменные в фигурные скобки. Там также можно использовать
# математические операции print(f" Мне {age+10} лет.").
# Однако не стоит писать громоздкие формулы сразу в вывод.
# Это ухудшает читаемость кода.