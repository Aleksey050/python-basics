DataList = []
obj = int(input('Введите количество обектов списка: '))
for i in range(0, obj):
    ele = input('Введите элемент списка: ')
    DataList.append(ele)
print(DataList)

a = 0
for i in range(int(len(DataList) / 2)):
    DataList[a], DataList[a + 1] = DataList[a + 1], DataList[a]
    a += 2

print(DataList)
