# Иван Васильевич пришел на рынок и решил купить два арбуза: один 
# для себя, а другой для тещи. Понятно, что для себя нужно выбрать
# арбуз потяжелей, а для тещи полегче. Но вот незадача: арбузов 
# слишком много и он не знает как же выбрать самый легкий и самый 
# тяжелый арбуз? Помогите ему!
# Пользователь вводит одно число N – количествоарбузов. Вторая 
# строка содержит N чисел,записанных на новой строчке каждое. 
# Здесь каждоечисло – это масса соответствующего арбуза

w = list(map(int, input('Введите вес арбуза через пробел: ').split()))
n = len(w)
min = w[0]
max = w[0]

for i in range(n):
    if min > w[i]:
        min = w[i]
    if max < w[i]:
        max = w[i]
print(f"Арбузов в наличии -> {w}")
print(f"Себе любимому -> {max}кг, тёще -> {min}кг")
