# Дано натуральное5 число. Требуется определиить,
# является ли год с данным номеров високосным. Если
# год является високосным, то выведите YES, иначе
# выведите NO. Напомним, что в соответствии с
# григорианским календарем, год является
# високосным, если его номер кратен 4, но не кратен
# 100, а также если он кратен 400.

# Iput: 2016
# Output: YES



print(' ')
i = int(input('Введите год: ', ))

if i%4==0 and i%100!=0:
    print(' ')
    print('YES')
    print(' ')
elif i%400==0:
    print(' ')
    print('YES')
    print(' ')
else:
    print(' ')
    print('NO')
    print(' ')












