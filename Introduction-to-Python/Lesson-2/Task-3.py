# 3. Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить, к какому времени года относится месяц (зима,
# весна, лето, осень). Напишите решения через list и dict.

month = int(input('Введите месяц '))

# 1
if month in [12, 1, 2]:
    print('Этот месяц относится к зиме.')
elif month in [3, 4, 5]:
    print('Этот месяц относится к весне.')
elif month in [6, 7, 8]:
    print('Этот месяц относится к лету.')
elif month in [9, 10, 11]:
    print('Этот месяц относится к осени.')
else:
    print('Такого месяца нет.')

# 2
year = {12: 'Зима', 1: 'Зима', 2: 'Зима', 3: 'Весна', 4: 'Весна', 5: 'Весна', 6: 'Лето', 7: 'Лето', 8: 'Лето',
        9: 'Осень', 10: 'Осень', 11: 'Осень'}
print(f'Месяц относитсня к времени года {year.get(month)}.')