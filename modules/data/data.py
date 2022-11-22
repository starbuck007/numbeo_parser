import requests
from bs4 import BeautifulSoup


def get_html(url):
    r = requests.get(url)
    return r.text


def get_list(html, element):
    soup = BeautifulSoup(html, 'lxml')
    t = soup.find(id=element).text.split('\n')
    s = []

    for i in t:
        if i in ['', '--- Select city---', '---Select country---', '---']:
            continue
        else:
            s.append(i)

    return s


def clean(data):
    data_upd = data.replace('\xa0', ' ').replace('\n', '').replace(',', '').replace('?', '').split(' ')[0]

    return data_upd


def get_info(html):
    res = []

    res_temp = {}
    category_temp = ''
    last_upd_temp = ''

    soup = BeautifulSoup(html, 'lxml')

    cur_currency = soup.find(id="displayCurrency").find(selected="selected")['value']

    last_update = soup.find(class_="align_like_price_table")
    l = []

    for i in last_update:
        j = i.text
        l.append(j)

        if 'Last update' in j:
            last_upd = j
            last_upd2 = last_upd.split(':')[1].replace('\n', '').replace(' ', ';').split(';')
            last_upd_temp = '{} {}'.format(last_upd2[1], last_upd2[2])

    t = soup.find(class_="data_wide_table new_bar_table").find_all("tr")

    for i in t:

        border = i.find(class_="category_icon_wrapper")
        category = i.find(class_="category_title")
        item = i.find("td")
        price = i.find(class_="first_currency")
        min_price = i.find(class_="barTextLeft")
        max_price = i.find(class_="barTextRight")
        bar = i.find(class_="priceBarTd")

        if border is None and category is None:

            if bar.text == '':

                min_price_final = ''
                max_price_final = ''


            else:

                min_price_final = clean(min_price.text)
                max_price_final = clean(max_price.text)

            res_temp = {'category': category_temp,
                        'item': item.text,
                        'currency': cur_currency,
                        'last update': last_upd_temp,
                        'price': clean(price.text),
                        'min_price': min_price_final,
                        'max_price': max_price_final}

            res.append(res_temp)

        else:

            category_temp = category.text

    return res


def check_price(price):
    new_price = False

    if price == '':
        new_price = None
    else:
        new_price = price

    return new_price
