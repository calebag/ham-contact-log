import sqlite3 as sql


def connect():
    return sql.connect('log.db')


def exit(connection):
    connection.commit()
    connection.close()


def create_entry_table():
    conn = connect()
    c = conn.cursor()

    with conn:
        c.execute('''CREATE TABLE IF NOT EXISTS log_entries (
            callsign TEXT,
            name TEXT,
            date TEXT,
            time TEXT,
            mode TEXT,
            band TEXT,
            country TEXT,
            state TEXT,
            city TEXT,
            coord_x REAL,
            coord_y REAL,
            talk_group TEXT,
            other TEXT
        )''')


def create_tags_table(name):
    """
    TODO: - finish and test tags system
          - use foreign key to add key table to main entry table
          - not necessarily a problem since this is offline, but look into better
            practices than " + name + ", can cause sql injection problems
    """

    conn = connect()
    c = conn.cursor()

    with conn:
        c.execute("CREATE TABLE IF NOT EXISTS tags_"+name+" (tags TEXT)")


def tag_insert(name, tags):
    conn = connect()
    c = conn.cursor()

    with conn:
        c.executemany("INSERT INTO " + name + " VALUES(?)", tags)


def insert(entry):
    conn = connect()
    c = conn.cursor()

    with conn:
        c.execute("INSERT INTO log_entries VALUES (:callsign, :name, :date, :time, :mode, :band, :country, :state, :city, :coord_x, :coord_y, :talk_group, :other)",
                  {'callsign': entry.callsign,
                   'name': entry.name,
                   'date': entry.date,
                   'time': entry.time,
                   'mode': entry.mode,
                   'band': entry.band,
                   'country': entry.country,
                   'state': entry.state,
                   'city': entry.city,
                   'coord_x': entry.coordinates[0],
                   'coord_y': entry.coordinates[1],
                   'talk_group': entry.talk_group,
                   'other': entry.other,
                   })


def show_entries():
    conn = connect()
    c = conn.cursor()

    with conn:
        c.execute("SELECT * FROM log_entries")
        print(c.fetchall())


def show_tags(name):
    conn = connect()
    c = conn.cursor()

    with conn:
        c.execute("SELECT rowid, * FROM " + name)
        print(c.fetchall())
