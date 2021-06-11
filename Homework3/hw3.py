# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов.
def my_func(a, b, c):
    if a > c and b > c:
        rez = a + b
    elif a > b and c > b:
        rez = a + c
    else:
        rez = b + c
    print(rez)

my_func(1, 2, 3)