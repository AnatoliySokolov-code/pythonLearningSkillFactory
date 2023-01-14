a = {1, 2, 3, 4, 5, 6, 7, 8}
b = {2, 4, 6, 8, 10, 12}
a_set, b_set = set(a), set(b)
a_and_b = a_set.symmetric_difference(b_set)
print(a_and_b)
#{1, 3, 5, 7, 10, 12}