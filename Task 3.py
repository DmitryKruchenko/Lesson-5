"""
Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс.,
вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.
"""

f_obj = open('test3.txt', 'r', encoding='utf-8')
lines = f_obj.readlines()
salary = 0
strings = 0
for line in lines:
    line_new = line.split()
    salary = salary + float(line_new[1])
    strings = strings + 1

    if (float(line_new[1]) < 20000):
        print(line_new[0])


print('Средняя заработная плата: ', salary / strings)

f_obj.close()