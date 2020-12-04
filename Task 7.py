"""
Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме: название,
форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
Подсказка: использовать менеджеры контекста.
"""
import json
with open("test7.txt", 'r', encoding='utf-8') as f_obj:
    lines = f_obj.readlines()
    profit = []
    companys = []

    profit_dict = {}
    averidge_profit_dict = {}
    data_base = [profit_dict, averidge_profit_dict]

    my_list = []
    numb_company = len(lines)

    for line in lines:
        txt = ''
        i = 0
        while i < len(line):                        # цикл превращения побуквенных элементов в список
            if line[i] != ' ':
                txt = txt + line[i]
            else:
                my_list.append(txt)
                txt = ''
            i = i + 1
        my_list.append(txt)
        #print(my_list)
        m = 0
    while m < numb_company:
        j = 2 + m * 4
        k = 3 + m * 4
        profit.append(float(my_list[j]) - float(my_list[k]))
        companys.append(my_list[m*4])
        m = m + 1
    #print(companys)
    #print(profit)

    profit_value = 0
    n = 0
    for x in profit:                                 # расчет средней прибыли без убытка
        if x < 0:
            continue
        else:
            profit_value = profit_value + x
            n = n + 1
    average_profit = profit_value / n
    #print(average_profit)
    i = 0
    while i < numb_company:
        profit_dict[companys[i]] = profit[i]
        i = i + 1
    averidge_profit_dict['average_profit'] = average_profit
    print(data_base)

with open("test7_1.json", "w", encoding='utf-8') as write_f:
    json.dump(data_base, write_f)
    json_str = json.dumps(data_base)
    print(json_str)





