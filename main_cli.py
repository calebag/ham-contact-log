import database as db
from entry import Entry


def main():
    thing = Entry('KA1ABC', 'Person', '10/29/2021', '22:53', 'FM', '2M', 'USA', 'CA', 'San Francisco', (37.776312768026465, -122.43274594372399), '',
                  '', ['test', 'example'])
    thing2 = Entry('KA2XYZ', 'John', '11/4/2021', '10:40', 'DMR', '2M', 'Canada', 'ON', 'Toronto', (43.64680443570099, -79.38762780998232),
                  'Worldwide', '', ['something', 'yeah'])
    thing3 = Entry('KA2AAA', 'Jacob', '11/5/2021', '11:28', 'SSB', '10M', 'Australia', 'NSW', 'Sydney', (-33.846585017276205, 151.20950608390393),
                   '', '', ['tag1', 'tag2'])

    # print(thing)
    db.create_entry_table()

    db.insert(thing)
    db.insert(thing2)
    db.insert(thing3)

    db.create_tags_table()

    db.tag_insert(thing.tags)
    db.tag_insert(thing2.tags)
    db.tag_insert(thing3.tags)

    db.create_join_table()

    # db.log_tag_insert(1, 1)
    # db.log_tag_insert(1, 2)
    #
    # db.log_tag_insert(2, 3)
    # db.log_tag_insert(2, 4)
    #
    # db.log_tag_insert(3, 4)
    # db.log_tag_insert(3, 5)

    # log_entry_input()

    db.show_entries()
    db.show_tags()
    db.show_log_tag_join()

    print(db.get_coordinates())


# temporary method of user input, will eventually be gui
# probably unnecessary, just wanted it in case
def log_entry_input():
    attrs = {}
    x = "y"
    new_thing = Entry('', '', '', '', '', '', '', '', '', [], '', '', [])

    while x != "n":
        for field in new_thing.__dict__.keys():
            attr = input("Enter " + field + ": ")
            attrs[field] = attr

        print(attrs)

        new_thing = Entry(attrs.get("callsign"), attrs.get("name"), attrs.get("date"), attrs.get("time"), attrs.get("mode"),
                          attrs.get("band"), attrs.get("country"), attrs.get("state"), attrs.get("city"),
                          tuple([float(i) for i in attrs.get("coordinates").split(",")]), attrs.get("talk_group"), attrs.get("other"), attrs.get("tags").split(","))

        db.insert(new_thing)
        db.tag_insert(new_thing.tags)

        x = input("Again? (y/n): ")


if __name__ == '__main__':
    main()

# 'KA1ABC', 'Person', '10/29/2021', '22:53', 'FM', '2M', 'USA', 'CA', 'San Francisco', [2.2, 1.1], '', '', ['test', 'example']
