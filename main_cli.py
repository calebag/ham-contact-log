import database as db
from entry import Entry


def main():
    thing = Entry('KA1ABC', 'Person', '10/29/2021', '22:53', 'FM', '2M', 'USA', 'CA', 'San Francisco', [2.2, 1.1], '', '', ['test', 'example'])
    # print(thing)
    db.create_entry_table()

    db.insert(thing)
    db.show_entries()

    tags = thing.tags

    db.create_tags_table()
    db.tag_insert(tags)
    db.show_tags()

    db.create_join_table()
    db.show_log_tag_join()


if __name__ == '__main__':
    main()

# 'KA1ABC', 'Person', '10/29/2021', '22:53', 'FM', '2M', 'USA', 'CA', 'San Francisco', [2.2, 1.1], '', '', ['test', 'example']
