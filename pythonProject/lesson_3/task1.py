# Напишите функцию modification(lst), которая принимает список и меняет местами его первый и последний элемент.
# В исходном списке минимум 2 элемента.
g = 0
def modification(lst):
    first_elem = lst[0]
    last_elem = lst[-1]
    lst[0] = last_elem
    lst[-1] = first_elem
    return lst

# Ниже НИЧЕГО НЕ НАДО ИЗМЕНЯТЬ


data = [
    [1, 2, 3],
    [1, 2, 3, 4, 5],
    ['н', 'л', 'о', 'с']
]

test_data = [
    [3, 2, 1], [5, 2, 3, 4, 1], ['с', 'л', 'о', 'н']
]


for i, d in enumerate(data):
    assert modification(d) == test_data[i], f'С набором {d} есть ошибка, не проходит проверку'
    print(f'Тестовый набор {d} прошёл проверку')
print('Всё ок')