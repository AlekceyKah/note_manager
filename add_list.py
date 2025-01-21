username = input('Введите фамилию: ') # username фамилия и имя студента ввод через input
title =  input('обозначение проекта: ') # title обозначение проекта 'Учебный проект'ввод через input
content =  input('описание проекта: ') # content описание проекта 'Работа с переменными'ввод через input
status =  input('статус проекта: ') # status статус проекта 'Активна' ввод через input
created_date =  input('дата начала проекта в формате день-месяц-год: ')
'''created_date дата начала проекта '13-01-2025' ввод через input
'''
issue_date =  input('дата окончания проекта в формате день-месяц-год: ')
'''issue_date дата окончания проекта'13-02-2025' ввод через input
'''
title_1 = input(f'заголовок  {1}: ') # title_1 первый заголовок проекта
title_2 = input(f'заголовок  {2}: ') # title_2 второй заголовок проекта
title_3 = input(f'заголовок  {3}: ') # title_3 третий заголовок проекта
title_s = [title_1, title_2, title_3] # title_s объединеие строк в список
print(username) # print функция вывода на экран
print(title)
print(content)
print(status)
print(created_date)
print(issue_date)
print(title_s)
