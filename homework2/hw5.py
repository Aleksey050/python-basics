rating_list = [8, 7, 7, 4, 4, 4, 2, 1]
new_rating = int(input('Введите новой числовое значение рейтинга: '))

max_new = max(rating_list)
if new_rating > max_new:
    rating_list.insert(-1, new_rating)
elif new_rating in rating_list:
    rating_list.insert(rating_list.index(new_rating), new_rating)
else:
    rating_list.append(new_rating)
print(rating_list)


