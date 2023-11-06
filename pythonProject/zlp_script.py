# Статистика букв
# Напишите функцию letter_stat, которая на вход принимает строку our_str и возращает словарь letters_dict,
# где в качестве ключей буквы строки, а значениями являются числа,
# соответствующие количеству вхождений данной буквы в строку.
# Например (Ввод --> Вывод) :
# 'letter' --> {'l': 1, 'e': 2, 't': 2, 'r': 1}
#
# my_dict = {'apple': 1, 'banana': 2, 'orange': 3}
# my_list = list(my_dict.items())
# my_string = ', '.join(map(str, my_list))
# print(my_string)


my_dict = {'apple': '1', 'banana': '2', 'orange': '3'}

my_string = ', '.join([str(key) + ': ' + str(value) for key, value in my_dict.items()])
print(my_string)
# cats_data =[('Мартин', 5, 'Алексей', 'Егоров'),
#  ('Фродо', 3, 'Анна', 'Самохина'),
#  ('Вася', 4, 'Алексей', 'Егоров')]
# dict_cats = {}
# our_str = []
# boss = []
# cats = []
# boss_dict = {}
#
# new_cats_data = []
# for i in range(len(cats_data)):
#     new_cats_data.append(list(cats_data[i]))
#     buffer = cats_data[i][2] +' ' + cats_data[i][3]
#     print(buffer)
#
#     del new_cats_data[i][2]
#     del new_cats_data[i][2]
#     # new_cats_data.pop(2)
#     # # new_cats_data.pop(3)
#     new_cats_data[i].append(buffer)




    # for j in range(len(cats_data[i])):
    #     new_cats_data.append(cats_data[i])

    # new_cats_data.append(cats_data[i])
    # for j in range(len(cats_data[i])):
    #     buffer = new_cats_data[j][2] + new_cats_data[j][3]
    #     new_cats_data[j][2] = new_cats_data[j][2] + new_cats_data[j][3]



# print(cats_data)
# print(new_cats_data)


# # Создаем словарь boss_dict из пустых ключей по ФИО
# for i in range(len(cats_data)):
#     boss.append(cats_data[i][2] + ' ' + cats_data[i][3])
# print(boss)
# boss_dict = {boss[i]: None for i in range(len(cats_data))}
# print(boss_dict)
#
# # Создаем список кошек
# for i in range(len(cats_data)):
#     cats.append(str(cats_data[i][0]) + ', ' + str(cats_data[i][1]))
# print(cats)
# print(boss_dict['Алексей Егоров'])
# # my_list = ['a', 'b', 'c']
# # my_dict = {boss[i]: None for i in range(len(my))}
# # print(my_dict)
#




# i=0
# zero = 0
# lst = [1, 2, 0, 1, 0, 1, 0, 3, 0, 1]
# while i < (len(lst)-zero):
#     print(lst)
#     if lst[i] == 0:
#         del lst[i]
#         lst.append(0)
#         zero += 1
#     else:
#         i += 1


        # del lst[i]








# while i < len(lst):
#     if lst[i] == 0:
#         del lst[i]
#         lst.append(0)
#     else:
#         i += 1

# for i in range(len(lst)):
#     if lst[i] == 0:
#         lst.append(lst.pop(i))