# Дано натуральное число. Требуется определить,
# является ли год с данным номером високосным. Если
# год является високосным, то выведите YES, иначе
# выведите NO. Напомним, что в соответствии с
# григорианским календарем, год является
# високосным, если его номер кратен 4, но не кратен
# 100, а также если он кратен 400.

yer = int(input('Введите год: '))

if yer % 4 == 0 and yer % 100 != 0 or yer % 400 == 0:
    print(f"Год {yer} високосный")
else:
    print(f"Год {yer} невисокосный")
