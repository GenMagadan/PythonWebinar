# За день машина проезжает n километров. Сколько
# дней нужно, чтобы проехать маршрут длиной m
# километров? При решении этой задачи нельзя
# пользоваться условной инструкцией if и циклами.

n = int(input('Введите скорость машина n: '))
m = int(input('Введите длину маршрута m: '))

print(m//n + 1 % (m % n + 1))
print((m + n - 1) // n)
