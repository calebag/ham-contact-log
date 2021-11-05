import sqlite3 as sql


def connect():
    return sql.connect('log.db')


def exit(connection):
    connection.commit()
    connection.close()


def create_entry_table():
    conn = connect()
    conn.execute("PRAGMA foreign_keys = 1")
    c = conn.cursor()

    with conn:
        c.execute('''CREATE TABLE IF NOT EXISTS log_entries (
            id INTEGER PRIMARY KEY NOT NULL,
            callsign TEXT NOT NULL,
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


def create_tags_table():
    conn = connect()
    conn.execute("PRAGMA foreign_keys = 1")
    c = conn.cursor()

    with conn:
        c.execute("CREATE TABLE IF NOT EXISTS tags_table (id INTEGER PRIMARY KEY NOT NULL, tag TEXT)")


def create_join_table():
    conn = connect()
    conn.execute("PRAGMA foreign_keys = 1")
    c = conn.cursor()

    with conn:
        c.execute('''CREATE TABLE IF NOT EXISTS log_tag_join (
        log_id INTEGER,
        tag_id INTEGER,
        FOREIGN KEY(log_id) REFERENCES log_entries(id),
        FOREIGN KEY(tag_id) REFERENCES tags_table(id)
        )''')


def tag_insert(tags):
    conn = connect()
    conn.execute("PRAGMA foreign_keys = 1")
    c = conn.cursor()

    tags = zip(iter(tags))

    with conn:
        c.executemany("INSERT INTO tags_table(tag) VALUES(?)", tags)


def insert(entry):
    conn = connect()
    conn.execute("PRAGMA foreign_keys = 1")
    c = conn.cursor()

    with conn:
        c.execute("INSERT INTO log_entries(callsign, name, date, time, mode, band, country, state, city, coord_x, coord_y, talk_group, other) VALUES (:callsign, :name, :date, :time, :mode, :band, :country, :state, :city, :coord_x, :coord_y, :talk_group, :other)",
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


def log_tag_insert(log_id, tag_id):
    conn = connect()
    conn.execute("PRAGMA foreign_keys = 1")
    c = conn.cursor()

    c.execute("INSERT INTO log_tag_join(log_id, tag_id) VALUES (:log_id, :tag_id)", (log_id, tag_id))


def show_entries():
    conn = connect()
    c = conn.cursor()

    with conn:
        c.execute("SELECT * FROM log_entries")
        print(c.fetchall())


def show_tags():
    conn = connect()
    c = conn.cursor()

    with conn:
        c.execute("SELECT * FROM tags_table")
        print(c.fetchall())


def show_log_tag_join():
    conn = connect()
    c = conn.cursor()

    with conn:
        c.execute("SELECT tag FROM log_entries CROSS JOIN tags_table")
        print(c.fetchall())
