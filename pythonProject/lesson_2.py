# Квест 1
# Дано 1 число - сторона квадрата. Напишите программу, которая рассчитает 3 значения:
# периметр квадрата, площадь квадрата и диагональ квадрата.
print ('Квест 1')
a = 5
print(a * 4)  #Периметр
print(a ** 2)  #Площадь
print(2 ** 0.5 * a)  #Длина диагонали


# Квест 2
# Дано квадратное уравнение x^2+bx+c=0.
# Дискриминант уравнения должен быть больше 0. Напишите программу, которая найдет корни
# квадратного уравнения и округлит их до 2 знаков после запятой.
print('')
print ('Квест 2')

b = 5
c = 4
D = (b**2 - 4*c)
print(D)

# Квест 3
# Дано 2 строки. Напишите программу, которая объединит эти две строки в одну и разделит их
# пробелом, а также поменяет местами первые два символа первой строки на первые два
# символа второй строки и наоборот.
print('')
print ('Квест 3')

str1 = ('Истринна в вине')
str2 = ('Считает каждый философ')
print(str1 + ' ' + str2)

print(str2[0] + str2[1] + str1[2:] + ' ' + str1[0] + str1[1]+ str2[2:])

# Квест 4
# Дан абсолютный путь до файла. Вывести название файла без расширения, названия диска и
# корневую папку.
print('')
print ('Квест 4')

file1 = r"C:\Users\egorl\Desktop\Курсы по АТ\Вебинар 2\Вебинар 2. Числа и строки в Python. 28.04.mp4"
file2 = file1.split('\\') # разбил на список
file3 = file2[-2] # Это переменная для корневой папки, чтобы не забить
file2 = file2[-1] # Переменная для имени файла полнгстью
file2 = file2[:file2.rfind('.')] # Нашел последнюю точку (где тип файла) и выкинул нафиг что после

print('Файл: ' + file2)
print('Диск: ' + file1[0])
print('Диск: ' + file1[:file1.find(':')]) #так просто игрался
print('Корневая папка: ' + file3)

# Квест 5
# Дано 2 числа a и b. Используя форматирование строк, выведите на экран их сумму и
# произведение в форматах ’a + b = c’ и ’a*b = c’.
print('')
print ('НЕ ГОТОВОКвест 5')

# Квест 6
# Дана строка. Напишите программу удаления символов, которые имеют нечетные значения
# индекса заданной строки.
print('')
print ('Квест 6')

strdelete = '12345678'
strresult=[]

for i in range(len(strdelete)):
    if i % 2 == 0:
        strresult.append(strdelete[i])
print(''.join(strresult))

# Квест 7
# Дано 2 строки из неповторяющихся символов: первая строка длиной 3 символа, вторая точно
# содержит символы первой строки в любом порядке. Напишите программу, не используя циклы
# и условия, которая находит срез минимальной длины во второй строке, который будет
# содержать все символы первой строки. Например,
# first_string = ‘wtf’ и second_string = ‘brick quz jmpy veldt whangs fox’, срез минимальной длины: ‘t whangs f’
print('')
print ('Квест 7')

first_string = 'wtf'
second_string = 'brick quz jmpy veldt whangs fox'

# Обозначили буквы
letter1 = first_string[0]
letter2 = first_string[1]
letter3 = first_string[2]

# Нашли их индекс
dot1 = second_string.find(letter1)
dot2 = second_string.find(letter2)
dot3 = second_string.find(letter3)

#Найдем максимальный и минимальный индекс. Средний будет между стопроц
dot = [dot1, dot2, dot3]
dotmax = max(dot)
dotmin = min(dot)

print(second_string[dotmin:dotmax+1])