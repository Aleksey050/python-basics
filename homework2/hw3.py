seasone = [
    [1, "Зима"],
    [2, "Зима"],
    [3, "Весна"],
    [4, "Весна"],
    [5, "Весна"],
    [6, "Лето"],
    [7, "Лето"],
    [8, "Лето"],
    [9, "Осень"],
    [10, "Осень"],
    [11, "Осень"],
    [12, "Зима"],
]
seasone_dict = dict(seasone)
# print(seasone_dict)
# print(seasone_dict[5])

month = int(input('Введите месяц в виде целого числа: '))
if month in seasone_dict:
    seas = seasone_dict[month]
    print(seas)