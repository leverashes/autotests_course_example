# Дан список. Найдите сумму элементом с четными индексами

# Да, понимаю что говнокод и мне не нравится, но работает.

# def filter_odd_num(in_num):
#     if(in_num.index() % 2) == 0:
#         return True
#     else:
#         return False

def even_sum(lst):
    # buffer = [] # Задали буффер обновления и при каждом цикле его обнуляем
    # for i in range(len(lst)):
    #     if i % 2 == 0:
    #         buffer.append(lst[i]) # Заполнили буфферный список только четными элементами
    #         sum_list = sum(buffer) # Просуммировали
    # sum_list = sum(filter(filter_odd_num, lst))
    # print(sum_list)
    sum_list = sum(filter(lambda x: x % 2 == 0, lst))
    return sum_list

# Ниже НИЧЕГО НЕ НАДО ИЗМЕНЯТЬ


data = [
    [1, 2, 3, 4, 5, 6, 7],
    [-1, -2, -3, -4, -5, -6, -7],
    [99, 56, 209, -308, -12, -18, 42],
    [-1, -2, -3, 0, 1, 2, 3],
]

test_data = [
    16, -16, 338, 0
]


for i, d in enumerate(data):
    assert even_sum(d) == test_data[i], f'С набором {d} есть ошибка, не проходит проверку'
    print(f'Тестовый набор {d} прошёл проверку')
print('Всё ок')


# strdelete = '12345678'
# strresult=[]
#
# for i in range(len(strdelete)):
#     if i % 2 == 0:
#         strresult.append(strdelete[i])
# print(''.join(strresult))