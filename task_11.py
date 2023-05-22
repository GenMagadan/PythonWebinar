# Дано натуральное число A > 1. Определите, каким по счету числом
# Фибоначчи оно является, то есть выведите такое число n, что
# φ(n)=A. Если А не является числом Фибоначчи, выведите число -1.

A = int(input('Введите натуральное число A больше 1: '))

status = True
num1 = 0
num2 = 1
i = 2

while status:
    result = num1 + num2
    num1 = num2
    num2 = result
    i += 1

    if A == result:
        print(i)
        status = False
    elif result > A:
        print(-1)
        status = False
