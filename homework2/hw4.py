text = input('Введите текст: ')
slp_text = text.split()
a = 1
for word in slp_text:
    print(a, word[0:10])
    a += 1

