# В некоторой школе решили набрать три новых
# математических класса и оборудовать кабинеты для
# них новыми партами. За каждой партой может сидеть
# два учащихся. Известно количество учащихся в
# каждом из трех классов. Выведите наименьшее
# число парт, которое нужно приобрести для них.

# Input: 20 21 22(ввод чисел НЕ в одну строку)
# Output: 32



# МОЙ ВАРИАНТ РЕШЕНИЯ
# import math

a = int(input('Введите первое число ', ))
b = int(input('Введите второе число ', ))
c = int(input('Введите третье число ', ))
# d = math.ceil(((a)+(b)+(c))/2)
# print('Минимальное количество парт, необходимое для оснащения классов ' '=', d, ' так как общее количество учеников составляет ', a+b+c)



# ВАРИАНТ РЕШЕНИЯ НА СЕМИНАРЕ
print('Минимальное количество парт, необходимое для оснащения классов ' '=', (a//2+a%2)+(b//2+b%2)+(c//2+c%2), ' так как общее количество учеников составляет ', a+b+c)










