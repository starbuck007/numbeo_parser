import modules.database.connect as connect


def find_city_country_id(name, country_id):
    name_id = False
    con, cur = connect.connect()
    res = cur.execute("select `id` from `cities` where `name` = %s and `country_id` = %s", (name, country_id))

    if res:
        row = cur.fetchone()
        name_id = row['id']

    con.close()

    return name_id


def insert(name, country_id):
    if find_city_country_id(name, country_id):
        return False

    con, cur = connect.connect()

    cur.execute("insert into `cities` (`name`, `country_id`) values (%s, %s)", (name, country_id))

    name_id = con.insert_id()

    con.commit()
    con.close()

    return name_id
