# Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B
# с помощью рекурсии.
#
# *Пример:*
#
# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8

# a = int(input('Введите число: '))
# b = int(input('Введите степень: '))
#
# def grade(n,m):
#  if m == 0:
#   return 1
#  else:
#   return n * grade(n, m - 1)
#
# print(grade(a, b))







# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
#
# *Пример:*
#
# 2 2
#     4

# a = int(input('Введите первое число: '))
# b = int(input('Введите второе число: '))
#
# def sum(n,m):
#  if m == 0:
#   return n
#  else:
#   return 1 + sum(n, m - 1)
#
# print(sum(a, b))
