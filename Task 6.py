"""
Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
практических и лабораторных занятий по этому предмету и их количество. Важно, чтобы для каждого предмета не обязательно
были все типы занятий. Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
Вывести словарь на экран.
Примеры строк файла:
Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —

Пример словаря:
{“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
"""
my_dict = {}
keys_dict = ''
f_obj = open('test6.txt', 'r', encoding='utf-8')

lines = f_obj.readlines()
for line in lines:
    i = 0
    txt1 = ''
    txt_list = []
    while i < len(line):
        if line[i] != ' ':
            txt1 = txt1 + line[i]
        else:
            txt_list.append(txt1)
            txt1 = ''
        i = i + 1

    txt_list.append(txt1)
    el1 = txt_list
    keys_dict = el1[0]
    el1.pop(0)
    el2 = ''
    el3 = ''
    my_sum = 0
    el4 = 0
    for x in el1:
        el2 = x
        i = 0
        while i < len(x):
            if el2[i] != '(':
                el3 = el3 + el2[i]
                i = i + 1
            else:
                el4 = int(el3)
                #print(el4)
                my_sum = my_sum + el4
                el3 =''
                el4 = 0
                break
        my_sum = my_sum + el4

    my_dict[keys_dict] = my_sum
print(my_dict)
    #print(keys_dict, my_sum)

f_obj.close()

