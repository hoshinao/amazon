import sqlite3
from contextlib import closing

dbname = 'database.db'
with closing(sqlite3.connect(dbname)) as connection:
    cursor = connection.cursor()
    sql = 'insert into test (id, name, mail) values (?,?,?)'
    data = (10, 'hoshikawa', 'test@gmail.com')
    cursor.execute(sql, data)
    connection.commit()
    connection.close()