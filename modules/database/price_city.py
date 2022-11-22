import modules.database.connect as connect


def insert_price(price, price_min, price_max, item_id, category_id, city_id, currency_id, last_update_id):
    con, cur = connect.connect()

    cur.execute("insert into `price_cities` "
                ""
                "(`price`, "
                "`price_min`, "
                "`price_max`, "
                "`item_id`, "
                "`category_id`, "
                "`city_id`, "
                "`currency_id`, "
                "`date_update_id`) "
                ""
                "values (%s, %s, %s, %s, %s, %s, %s, %s)",
                (price, price_min, price_max, item_id, category_id, city_id, currency_id, last_update_id))

    price_id = con.insert_id()

    con.commit()
    con.close()

    return price_id
