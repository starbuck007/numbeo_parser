import modules.database.connect as connect


def find_date_update(last_update):
    name_id = False
    con, cur = connect.connect()
    res = cur.execute("select `id` from `date_updates` where `last_update` = %s", last_update)

    if res:
        row = cur.fetchone()
        name_id = row['id']

    con.close()

    return name_id


def insert(last_update):
    if find_date_update(last_update):
        return False

    con, cur = connect.connect()

    cur.execute("insert into `date_updates` (`last_update`) values (%s)", last_update)

    name_id = con.insert_id()

    con.commit()
    con.close()

    return name_id
