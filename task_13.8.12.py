# Напишите программу, которая на вход принимает последовательность
# целых чисел и возвращает True, если все числа равны нулю, и False,
# если найдется хотя бы одно ненулевое число. Разрешается использование
# только логических операторов и функций all([ ]) и any([ ]).
L = list(map(int, input().split()))

print(not any(L))