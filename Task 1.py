"""
1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""

lines = []
i = True
while i:
   i = input()
   if i:
       lines.append(i)
print(lines)

with open("test1.txt", "w", encoding='utf-8') as file:
    for  line in lines:
        #input(line)
        file.write(line + '\n')
