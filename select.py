import sqlite3
from contextlib import closing

dbname = 'database.db'
with closing(sqlite3.connect(dbname)) as connection:
    cursor = connection.cursor()
    sql = 'select * from test where name = ? '
    data = ('hoshikawa', )
    for row in cursor.execute(sql, data):
        print(row)
    connection.close()