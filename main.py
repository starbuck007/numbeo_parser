import modules.data.data as data
import modules.database.country as db_country
import modules.database.city as db_city
import modules.database.currency as db_currency
import modules.database.category as db_category
import modules.database.item as db_item
import modules.database.update as db_update
import modules.database.price_country as db_price_country
import modules.database.price_city as db_price_city

url = 'https://www.numbeo.com/cost-of-living/in/Horsens?displayCurrency=EUR'
place = 'Denmark'
city = 'Horsens'

countries = data.get_list(data.get_html('https://www.numbeo.com/cost-of-living/'), 'country')

for country in countries:
    db_country.insert(country)

cities = data.get_list(data.get_html(url), 'city')

country_id = db_country.find_country_id(place)

for city in cities:
    db_city.insert(city, country_id)

currencies = data.get_list(data.get_html(url), 'displayCurrency')

for currency in currencies:
    db_currency.insert(currency)

info = data.get_info(data.get_html(url))

for i in info:

    db_category.insert(i['category'])
    category_id = db_category.find_category_id(i['category'])

    db_item.insert(i['item'], category_id)
    item_id = db_item.find_item_category_id(i['item'], category_id)

    db_update.insert(i['last update'])
    last_update_id = db_update.find_date_update(i['last update'])

    currency_id = db_currency.find_currency_id(i['currency'])

    price = data.check_price(i['price'])
    min_price = data.check_price(i['min_price'])
    max_price = data.check_price(i['max_price'])

    if 'country=' in url:
        db_price_country.insert_price(price, min_price, max_price, item_id, category_id, country_id, currency_id,
                                      last_update_id)

    else:

        city_id = db_city.find_city_country_id(city, country_id)

        db_price_city.insert_price(price, min_price, max_price, item_id, category_id, city_id, currency_id,
                                   last_update_id)
