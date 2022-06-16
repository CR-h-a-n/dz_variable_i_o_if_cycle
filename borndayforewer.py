# Дата рождения А.С. Пушкина 6 июня 1799 г.

indicator = False   # Указатель дан ли верный ответ

while indicator == False:   # Пока не дан верный ответ
    year = input('В каком году родился  Пушкин А.С.? Ваш ответ: ')

    if year.isnumeric():
        if int(year) == 1799:
            indicator = True    # Верный ответ дан
        else:
            print('Вы ошиблись.')
            print('Попробуйте ещё раз.')
    else:
        print('Вы ввели не корректное значение года.')
        print('Попробуйте ещё раз.')


indicator = False  # Обнуляем указатель дан ли верный ответ
while indicator == False:   # Пока не дан верный ответ
    month = input('В каком месяце родился  Пушкин А.С.? Ваш ответ: ')
    month_all = ('06', '6', 'июнь', 'июня', 'в июне', 'в шестом', 'шесть', 'шестого', 'шестом')
    if month.lower() in month_all:
        indicator = True  # Верный ответ дан
    else:
        print('Неверный месяц.')
        print('Попробуйте ещё раз.')


indicator = False  # Обнуляем указатель дан ли верный ответ
while indicator == False:   # Пока не дан верный ответ
    day = input('Какого числа родился  Пушкин А.С.? Ваш ответ: ')
    day_all = ('06', '6', 'шесть', 'шестого', 'шестое')
    if day.lower() in day_all:
        indicator = True  # Верный ответ дан
    else:
        print('Неверный день.')
        print('Попробуйте ещё раз.')


print('Всё верно!')