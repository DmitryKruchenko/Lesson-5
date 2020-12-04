"""
Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские. Новый блок строк должен записываться в новый
текстовый файл.
"""

f_obj = open('test4.txt', 'r', encoding='utf-8')
lines = f_obj.readlines()
print(lines)
lines_new = []

f_obj_new = open('test4_1.txt', 'w', encoding='utf-8')
i = 1
for line in lines:
    if i == 1:
        lines_new.append(line.replace('One', 'Один'))
    if i == 2:
        lines_new.append(line.replace('Two', 'Два'))
    if i == 3:
        lines_new.append(line.replace('Three', 'Три'))
    if i == 4:
        lines_new.append(line.replace('Four', 'Четыре'))
    i = i + 1

print(lines_new)
f_obj_new.writelines(lines_new)
f_obj_new.close()
f_obj.close()