"""
Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""
lines = []


lines.append(input('введите любые числа, разделяя их пробелом: ', ))
#print(lines)

with open("test5.txt", "w", encoding='utf-8') as file:
    i = 0
    for  line in lines:

        file.write(line)

f_obj = open('test5.txt')
txt = f_obj.read()
txt1 = ''
my_sum = 0
i = 0
while i < len(txt):
    if txt[i] != ' ':
        txt1 = txt1 + txt[i]
    else:
        my_sum = my_sum + int(txt1)
        txt1 = ''
    i = i + 1
my_sum = my_sum + int(txt1)
print(my_sum)
f_obj.close()