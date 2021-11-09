import sqlite3
from contextlib import closing
dbname = 'database.db'

with closing(sqlite3.connect(dbname)) as connection:
    cursor = connection.cursor()
    sql = 'create table test (id int, name varchar(64), mail varchar(1024))'
    cursor.execute(sql)
    connection.commit()
    connection.close()