from collections import Counter
from openpyxl import load_workbook
import pandas
from utils import *



def make_report(log_file, report_template, report_output):
    
    wb = load_workbook(report_template) # open existing workbook


    ws = wb.active # trans in variable active sheet


    read_logs = pandas.read_excel(log_file)
    logs_dict = read_logs.to_dict(orient='records')


    browsers = all_browsers(logs_dict) # словарь всех браузеров с посещением помесячно
    _visits_of_browsers = visits_of_browsers(logs_dict) # словарь всех браузеров с посещениями за весь период
    _sorted_visits_of_browser = sorted_visits_of_browser(_visits_of_browsers) # сортировка посещений браузеров в обратном порядке
    _raiting_of_browsers = raiting_of_browsers(_visits_of_browsers, _sorted_visits_of_browser) # 7 самых популярных браузеров
    _res_browsers = res_browsers(_raiting_of_browsers, browsers) # 7 самых популярных браузеров с посещениями по месяцам


    goods = all_goods(logs_dict) # словарь всех товаров с их покупками помесячно
    _buyings_of_goods = buyings_of_goods(logs_dict) # словарь всех товаров с их покупками за весь период
    _sorted_buyings_of_goods = sorted_buyings_of_goods(_buyings_of_goods) # сортировка товаров по покупкам в обратном порядке
    _raiting_of_goods = raiting_of_goods(_buyings_of_goods, _sorted_buyings_of_goods) # 7 самых популярных товаров
    _res_goods = res_goods(_raiting_of_goods, goods) # 7 самых популярных товаров по месяцам


    _mens_choice = mens_choice(logs_dict) # список предпочтений мужчин
    _mens_goods_dict = Counter(_mens_choice) # словарь с количеством покупок предпочтений мужчин


    _women_choice = women_choice(logs_dict) # список предпочтений женщин
    _women_goods_dict = Counter(_women_choice) # словарь с количеством покупок предпочтений женщин

    
    # заполнение эксел файла - топ 7 браузеров по убыванию с помесячными посещениями
    row_browsers = 5
    for key in _res_browsers:
        _ = ws.cell(column=1, row=row_browsers, value=key)
        for value in _res_browsers[key]:
            _ = ws.cell(column=int(value)+1, row=row_browsers, value=_res_browsers[key][value])
        row_browsers += 1

    # заполнение эксел файла - топ 7 браузеров по убыванию с помесячными посещениями
    row_goods = 19
    for key in _res_goods:
        _ = ws.cell(column=1, row=row_goods, value=key)
        for value in _res_goods[key]:
            _ = ws.cell(column=int(value)+1, row=row_goods, value=_res_goods[key][value])
        row_goods += 1

    # популярные и непопулярные товары у мужчин и женщин
    ws['B31'] = mens_popular_goods(_mens_goods_dict)
    ws['B32'] = women_popular_goods(_women_goods_dict)
    ws['B33'] = mens_useless_goods(_mens_goods_dict)
    ws['B34'] = women_useless_goods(_women_goods_dict)


    wb.save(report_output)

