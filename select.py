# AULA 394 - Consulta a base de dados
import sqlite3

from main import DB_FILE, TABLE_NAME

connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

cursor.execute(
    f'SELECT * FROM {TABLE_NAME} '
)

# # row => linha
for row in cursor.fetchall():
#     # _id = row[0]
#     # name = row[1]
#     # weight = row[2]

    ### Desempacotamento da tupla
    _id, name, weight = row
    print(_id, name, weight)

print()

cursor.execute(
    f'SELECT * FROM {TABLE_NAME} '
    'WHERE id = "3"'
)

row = cursor.fetchone()
_id, name, weight = row
print(_id, name, weight)

# OBS: O Cursor esgota!
 
cursor.close()
connection.close()