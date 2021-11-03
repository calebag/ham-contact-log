import database as db
from entry import Entry


def main():
    db.create_entry_table()
    thing = Entry('KA1ABC', 'Person', '10/29/2021', '22:53', 'FM', '2M', 'USA', 'CA', 'San Francisco', [2.2, 1.1], '', '', ['test', 'example'])
    db.insert(thing)
    db.show_entries()

    name = thing.callsign  # Table's name = entry's callsign
    tags = ["test", "ok", "yeah"]
    tags = list(zip(*[iter(tags)]))  # turn tags list into list of tuples for SQL

    db.create_tags_table(name)
    db.tag_insert("tags_" + name, tags)
    db.show_tags("tags_" + name)


if __name__ == '__main__':
    main()

# 'KA1ABC', 'Person', '10/29/2021', '22:53', 'FM', '2M', 'USA', 'CA', 'San Francisco', [2.2, 1.1], '', '', ['test', 'example']
