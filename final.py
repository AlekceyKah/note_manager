username= input('Введите фамилию: ') # username фамилия и имя студента ввод через input
title = input('обозначение проекта: ') # title обозначение проекта 'Учебный проект'ввод через input
content =  input('описание проекта: ') # content описание проекта 'Работа с переменными'ввод через input
status =  input('статус проекта: ') # status статус проекта 'Активна' ввод через input
created_date =  input('дата начала проекта в формате день-месяц-год: ')
issue_date =  input('дата окончания проекта в формате день-месяц-год: ')
''' created_date, issue_date: ввод данных в формате формате день-месяц-год через input'''
project = [username, title, content, status, created_date,  issue_date]
title_1 = input(f"заголовок: {1} ") # info_1 первый заголовок проекта
title_2 = input(f"заголовок: {2} ") # info_2 второй заголовок проекта
title_3 = input(f"заголовок: {3} ") # info_3 третий заголовок проекта
title_s = [title_1, title_2, title_3]  # title_s объединение строк в список
project.append(title_s)
''' project.append(title_string) # добавление вложенных элементов списка title_s с помощью метода .append
'''
print(project[0]) # индексация и вывод списка в консоль
print(project[1])
print(project[2])
print(project[3])
print(project[4])
print(project[5])
print(project[6])