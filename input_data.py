import sqlite3


def c(value):
    if value.startswith("~"):
        return value.strip('~')
    if not value:
        value = "0"
    return float(value)


cc = sqlite3.connect('cars.db')
curs = cc.cursor()

curs.execute('''
CREATE TABLE food (
id      TEXT        PRIMERY KEY
dec     TEXT,
bmw     TEXT, 
audi    TEXT,
gas     TEXT,
washer  TEXT
''')

q = "INSERT INTO fod VALUES (?,?,?,?,?,?,?,?,?,?,?,?)"

for line in open ('file.txt'):
    fields = line.split('^')
    vals = [convert(f) for f in fields[:field_count]]
    curs.execute(query, vals)


conn.commit()
conn.close()