# Задание 14.1.3
# Напишите функцию, которая печатает «обратную лесенку» следующего типа:
# n = 3
# ***
# **
# *
#
# n = 4
# ****
# ***
# **
# *
def reverse_stair(n):
   for i in range(n, 0, -1):
       print("*" * i)

reverse_stair(3)
reverse_stair(4)
