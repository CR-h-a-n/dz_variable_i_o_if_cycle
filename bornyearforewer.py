# Дата рождения А.С. Пушкина 6 июня 1799 г.

indicator = False   # Указатель дан ли верный ответ

while indicator == False:   # Пока не дан верный ответ
    year = input('В каком году родился  Пушкин А.С.? Ваш ответ: ')

    if year.isnumeric():
        if int(year) == 1799:
            print('Верно!')
            indicator = True    # Верный ответ дан
        else:
            print('Вы ошиблись.')
            print('Попробуйте ещё раз.')
    else:
        print('Вы ввели не корректное значение года.')
        print('Попробуйте ещё раз.')