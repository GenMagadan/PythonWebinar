# По данному целому неотрицательному n вычислите значение n!.
# N! = 1 * 2 * 3 * … * N (произведение всех чисел от 1 до N)
# 0! = 1
# Решить задачу используя цикл while

N = int(input('Введите число N: '))

n = N
fact = 1
if n < 0:
    print('Введено некорректное отрицательное число')
else:
    while n > 1:
        fact *= n
        n -= 1
    print(f"факториал числа {N} = {fact}")
