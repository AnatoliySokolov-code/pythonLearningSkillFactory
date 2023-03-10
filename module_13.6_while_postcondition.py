# Работая с циклом while, нужно быть внимательным, ведь если условие
# остановки будет всегда True, то цикл никогда не остановится.
# Бывают задачи, в которых это полезно, например, вы создаёте программу,
# которая будет бесконечно обновлять и отображать время.
# Но зачастую бесконечный цикл — это ошибка начинающего программиста, который
# забыл добавить изменение условия цикла.

# плохо
# n = 1
# while n < 10:  # в данной программе это условие всегда True, цикл будет
# бесконечным
#     print("Hello World")
# Чтобы остановить выполнение такого скрипта в терминале нужно нажать Ctrl+C.
#
# Как уже обсуждалось, бывают моменты, когда необходимо специально
# запустить бесконечный цикл, но возникает вопрос, как его потом оставить,
# не отключая весь скрипт? Для это есть ключевое слово break,
# которое говорит, что цикл нужно принудительно прервать.

# хорошо
n = 1
while True:  # в данной программе это условие всегда True, цикл будет бесконечным
   print("Hello World")
   n += 1
   if n > 10:  # условие, при достижении которого цикл while будет принудительно завершен
       break
# Особенность использования такого цикла while с условием внутри заключается в том, что тело цикла точно выполнится один раз, в отличии от цикла с предусловием. Такой цикл ещё называют цикл с постусловием.