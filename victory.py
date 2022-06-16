questions = {'А.С. Пушкина' : '1799', # А.С. Пушкина 1799 г. поэт
            'В.В. Путин' : '1952',    # В.В. Путин 1952 г. президент РФ
            'А.М. Овечкин' : '1985',  # А.М. Овечкин 1985 г. хоккеист
            'Ф.Ф. Конюхов' : '1951',  # Ф.Ф. Конюхов 1951 г. путешественник
            'Сильве́стр Сталло́не' : '1946',  # Майкл Сильве́стр Гарденцио Сталло́не :))) 1946 г. актёр
            'Г.В. Лепс' : '1962'  # Г.В. Лепс 1962 г. певец
            }

repeat_quiz = True    # Указатель повтора викторины
key = questions.keys()  # Берём ключи словаря для создания вопросов

while repeat_quiz == True:
    count_all = 0
    count_right = 0
    for name in key:
        count_all += 1
        print('Вопрос №', count_all, sep='')
        if input('В каком году родился ' + name + '? Ваш ответ: ') == questions[name]:
            count_right += 1
        print('-' * 50)

    print('Kоличество правильных ответов:', count_right, '(', round(count_right / count_all * 100, 2),'%)')
    print('Kоличество ошибок:', count_all - count_right, '(', round((count_all - count_right) / count_all * 100, 2),'%)')

    indicator = False   # Указатель принят ли ответ о повторении викторины
    while indicator == False:
        answer = input('Хотите повторить викторину? Ваш ответ (д/н): ').lower()
        if answer in ['да', 'д', 'y', 'yes', '1']:
            repeat_quiz = True  # Повторить викторину
            indicator = True
        elif answer in ['нет', 'н', 'n', 'no', '0']:
            repeat_quiz = False     # Завершить викторину
            indicator = True
        else:
            print('Не понял Ваш ответ...')  # Переспросить, что делать
