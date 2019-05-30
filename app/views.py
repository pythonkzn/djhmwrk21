from django.shortcuts import render
import csv
from pprint import pprint

def inflation_view(request):
    data_list = []
    template_name = 'inflation.html'
    i = 0
    with open('inflation_russia.csv', encoding='utf8', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        for rows in reader:
            i+=1
            if i!=1:
                buf_rows = [float(x) for x in rows if (x != '') and (x != rows[0])]
                buf_rows.insert(0,rows[0])
                data_list.append(buf_rows)
    for list in data_list:
        if len(list) < 14:
            list.insert(len(list)+1, '')
            list.insert(len(list) + 1, '')
            list.insert(len(list) + 1, '')
            list.insert(len(list) + 1, '')
    head_list = ['Год','Янв', 'Фев', 'Мар', 'Апр', 'Май', 'Июн', 'Июл', 'Авг', 'Сен', 'Окт', 'Ноя', 'Дек', 'Суммарная']

    # чтение csv-файла и заполнение контекста
    context =  {'head_list': head_list,
                'data_list': data_list}

    return render(request, template_name,
                  context)