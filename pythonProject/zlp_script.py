# Напишите алгоритм, который берет список lst и перемещает все нули в конец, сохраняя порядок остальных элементов.
# Например (Ввод --> Вывод) :
# [1, 0, 1, 2, 0, 1, 3]  => [1, 1, 2, 1, 3, 0, 0]


i=0
zero = 0
lst = [1, 2, 0, 1, 0, 1, 0, 3, 0, 1]
while i < (len(lst)-zero):
    print(lst)
    if lst[i] == 0:
        del lst[i]
        lst.append(0)
        zero += 1
    else:
        i += 1


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