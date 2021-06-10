products = [
    (1, {"название": "ноутбук", "цена": "50000", "количество": "5", "единици": "шт."}),
    (2, {"название": "колонка", "цена": "4000", "количество": "13", "единици": "шт."}),
    (3, {"название": "камера", "цена": "7000", "количество": "9", "единици": "шт."}),
    (4, {"название": "микрафон", "цена": "3000", "количество": "10", "единици": "шт."})
]
# print(products[1][1])
title = []
price = []
sum = []
units = []

# for i in products:
#     print(i)

# print(products[1][1])
# title = products[1][1]
# print(title)

# key = "название"
# for i in products:
#     title = products[i][1].pop(key)
#     print(title)

key = "название"
i = 0
while i < len(products):
    title.append(products[i][1].pop(key))
    i += 1
print(key,':', title)

key = "цена"
i = 0
while i < len(products):
    price.append(products[i][1].pop(key))
    i += 1
print(key,':', price)

key = "количество"
i = 0
while i < len(products):
    sum.append(products[i][1].pop(key))
    i += 1
print(key,':', sum)

key = "единици"
i = 0
while i < len(products):
    units.append(products[i][1].pop(key))
    i += 1
print(key,':', units)