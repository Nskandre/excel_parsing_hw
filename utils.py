


# словарь всех браузеров с посещением помесячно
def all_browsers(my_dict): 
    browsers = {}
    for i in my_dict:
        if i['Браузер'] in browsers:
            browsers[i['Браузер']][str(i['Дата посещения'].month)] = browsers[i['Браузер']].get(
                str(i['Дата посещения'].month), 0) + 1
        else:
            browsers[i['Браузер']] = {
                str(i['Дата посещения'].month): browsers.get(str(i['Дата посещения'].month), 0) + 1}
    return browsers


# словарь всех браузеров с посещениями за весь период
def visits_of_browsers(my_dict):
    visits_of_browser = {}
    for i in my_dict:
        visits_of_browser[i['Браузер']] = visits_of_browser.get(i['Браузер'], 0) + 1
    return visits_of_browser


# сортировка посещений браузеров в обратном порядке
def sorted_visits_of_browser(visits_of_browsers):
    return sorted(visits_of_browsers.values(), reverse=True)


# 7 самых популярных браузеров
def raiting_of_browsers(visits_of_browsers, sorted_visits_of_browser):
    raiting_of_browsers = {}
    for i in sorted_visits_of_browser:
        for browser in visits_of_browsers.keys():
            if visits_of_browsers[browser] == i:
                raiting_of_browsers[browser] = i
            if len(raiting_of_browsers) >= 7:
                break
        if len(raiting_of_browsers) >= 7:
                break
    return raiting_of_browsers


# 7 самых популярных браузеров с посещениями по месяцам
def res_browsers(raiting_of_browsers, all_browsers):
    res_browsers = {}
    for browser in raiting_of_browsers.keys():
        res_browsers[browser] = all_browsers[browser]
    return res_browsers


# словарь всех товаров с их покупками помесячно
def all_goods(my_dict):
    goods = {}
    for i in my_dict:
        for j in i['Купленные товары'].split(','):
            if j.rstrip() in goods:
                goods[j.rstrip()][str(i['Дата посещения'].month)] = goods[j.rstrip()].get(str(i['Дата посещения'].month), 0) + 1
            else:
                goods[j.rstrip()] = {str(i['Дата посещения'].month): goods.get(str(i['Дата посещения'].month), 0) + 1}
    return goods


# словарь всех товаров с их покупками за весь период
def buyings_of_goods(my_dict):
    buyings_of_goods = {}
    for i in my_dict:
        for j in i['Купленные товары'].split(','):
            buyings_of_goods[j.rstrip()] = buyings_of_goods.get(j.rstrip(), 0) + 1
    return buyings_of_goods


# сортировка товаров по покупкам в обратном порядке
def sorted_buyings_of_goods(buyings_of_goods):
    return sorted(buyings_of_goods.values(), reverse=True)


# 7 самых популярных товаров
def raiting_of_goods(buyings_of_goods, sorted_buyings_of_goods):
    raiting_of_goods = {}
    for i in sorted_buyings_of_goods:
        for good in buyings_of_goods.keys():
            if buyings_of_goods[good] == i:
                raiting_of_goods[good] = i
            if len(raiting_of_goods) >= 7:
                break
        if len(raiting_of_goods) >= 7:
                break
    return raiting_of_goods


# 7 самых популярных товаров по месяцам
def res_goods(raiting_of_goods, goods):
    res_goods = {}
    for good in raiting_of_goods.keys():
        res_goods[good] = goods[good]
    return res_goods


# список предпочтений мужчин
def mens_choice(my_dict):
    mens_goods = []
    for i in my_dict:
        if i['Пол'] == 'м':
            for good in i['Купленные товары'].split(','):
                mens_goods.append(good.rstrip())
    return mens_goods


# самый популярный товар у мужчин
def mens_popular_goods(mens_goods_dict):
    mens_popular_goods = ''
    for good in mens_goods_dict:
        if len(mens_popular_goods) == 0 or mens_goods_dict[good] > mens_goods_dict[mens_popular_goods]:
            mens_popular_goods = good
    return mens_popular_goods
        

# самый не востребованный товар у мужчин
def mens_useless_goods(mens_goods_dict):
    mens_useless_goods = ''
    for good in mens_goods_dict:
        if len(mens_useless_goods) == 0 or mens_goods_dict[good] < mens_goods_dict[mens_useless_goods]:
            mens_useless_goods = good
    return mens_useless_goods


# список предпочтений женщин
def women_choice(my_dict):
    women_goods = []
    for i in my_dict:
        if i['Пол'] == 'ж':
            for good in i['Купленные товары'].split(','):
                women_goods.append(good.rstrip())
    return women_goods


# самый популярный товар у женщин
def women_popular_goods(women_goods_dict):
    women_popular_goods = ''
    for good in women_goods_dict:
        if len(women_popular_goods) == 0 or women_goods_dict[good] > women_goods_dict[women_popular_goods]:
            women_popular_goods = good
    return women_popular_goods
        

# самый не востребованный товар у женщин
def women_useless_goods(women_goods_dict):
    women_useless_goods = ''
    for good in women_goods_dict:
        if len(women_useless_goods) == 0 or women_goods_dict[good] < women_goods_dict[women_useless_goods]:
            women_useless_goods = good
    return women_useless_goods
