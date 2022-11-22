import modules.database.connect as connect


def find_item_category_id(name, category_id):
    name_id = False
    con, cur = connect.connect()
    res = cur.execute("select `id` from `items` where `name` = %s and `category_id` = %s", (name, category_id))

    if res:
        row = cur.fetchone()
        name_id = row['id']

    con.close()

    return name_id


def insert(name, category_id):
    if find_item_category_id(name, category_id):
        return False

    con, cur = connect.connect()

    cur.execute("insert into `items` (`name`, `category_id`) values (%s, %s)", (name, category_id))

    name_id = con.insert_id()

    con.commit()
    con.close()

    return name_id
