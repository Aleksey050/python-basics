# 1) Запрос и создание переменных
a = 10
b = 24
print(a, b)
name = input('Введите имя: ')
years = int(input('Введите возраст: '))
print("Меня зовут",name, ", мне",years, "года")

# 2) Перевод секунд в формат ЧЧ:ММ:СС
sec = int(input('Введите время в секундах: '))
hour = sec // 3600
minutes = (sec // 60) %60
second = sec %60
print(hour,':',minutes,':',second)

# 3) Найти сумму чисел n+nn+nnn
n = input('Ввидите число: ')
a = int(n)
b = int(n + n)
c = int(n + n + n)
d = a + b + c
print(d)

# 4) Найти самую большую цифр
num = int(input('Введите целое число: '))
avb = 0
while num >= 1:
    i = num % 10
    num = num // 10
    if i > avb:
        avb = i
print(avb)

# Добавил коментарий
# 5) фирмА)
rev = int(input('Выручка: '))
cost = int(input('Затраты: '))
if rev > cost:
    print('Прибыль - выручка больше затрат')
    pro = rev - cost
    staff = int(input('Ввидите число сотрудников: '))
    pay = pro / staff
    print('Доход одного сотрудника', pay)
else:
    print('Убыток - затраты больше выручки')

# 6) Спортсмен
a = int(input('Сколько км пробежал спортсмен в 1-й день: '))
b = int(input('Сколько км должен пробежать спортсмен: '))
d = 1
while a < b:
     a = a + (a / 10)
     d = d + 1
print(d)

