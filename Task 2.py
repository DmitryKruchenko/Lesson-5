"""
Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.

"""

lines = []
i = True
while i:
   i = input()
   if i:
       lines.append(i)

with open('test2.txt', 'w', encoding='utf-8') as file:
    for  line in lines:
        file.write(line + '\n')

f_obj = open('test2.txt')



lines_new = f_obj.readlines()
for line in lines_new:

    words_in_line = len(line.split())
    print('Слов в строке: ',  words_in_line)
    print('Букв в строке', len(line) - words_in_line)


f_obj.close()