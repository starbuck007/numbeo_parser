import modules.database.connect as connect


def find_category_id(name):
    name_id = False
    con, cur = connect.connect()
    res = cur.execute("select `id` from `categories` where `name` = %s", name)

    if res:
        row = cur.fetchone()
        name_id = row['id']

    con.close()

    return name_id


def insert(name):
    if find_category_id(name):
        return False

    con, cur = connect.connect()

    cur.execute("insert into `categories` (`name`) values (%s)", name)

    name_id = con.insert_id()

    con.commit()
    con.close()

    return name_id
