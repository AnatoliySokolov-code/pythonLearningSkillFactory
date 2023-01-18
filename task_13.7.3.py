# Skillfactory | Задача по Python
# Допишите функцию print_ladder так,
# чтобы она для числа n печатала лесенку следующего типа:
#
# n = 3
# *
# **
# ***
# n = 4
# *
# **
# ***
# ****
# ниже будет работать без этого цикла в задании
# N = 3
# for i in range(1, N + 1):
#    print("*" * i)
# N =4
# for i in range(1, N + 1):
#    print("*" * i)


def print_ladder(n):
       for i in range(1, n + 1):
        print('*' * i)

