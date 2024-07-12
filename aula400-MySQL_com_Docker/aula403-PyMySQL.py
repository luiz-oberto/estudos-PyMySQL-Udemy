# PyMySQL - um cliente MySQL feito em Python Puro 
# AULAS: 403, 404, 405, 406, 407, 408, 409, 410, 411, 412, 413, 414
# lembrando: O MariaDB é um fork do MySQL, ou seja, eles funcionam quase que de maneira similar
# pip install pymysql
import pymysql
import dotenv
import os

TABLE_NAME = 'customers'

dotenv.load_dotenv()

connection = pymysql.connect(
    host=os.environ['MYSQL_HOST'],
    user=os.environ['MYSQL_USER'],
    password=os.environ['MYSQL_PASSWORD'],
    database=os.environ['MYSQL_DATABASE'],
)

print(os.environ['MYSQL_DATABASE'])

with connection:
    with connection.cursor() as cursor:
        cursor.execute( # type: ignore
            # cria tabela
            'CREATE TABLE IF NOT EXISTS customers ('
            'id INT NOT NULL AUTO_INCREMENT, '
            'nome VARCHAR(50) NOT NULL, '
            'idade INT NOT NULL, '
            'PRIMARY KEY (id) '
            ') '
        )
        # CUIDADO: ISSO LIMPA A TABELA
        cursor.execute(f'TRUNCATE TABLE {TABLE_NAME}')
    connection.commit()

    # Começo a manipular dados a partir daqui

    # inserindo um valor usando placeholder e um iterável
    with connection.cursor() as cursor:
        sql = (
            f'INSERT INTO {TABLE_NAME} '
            '(nome, idade) '
            'VALUES '
            '(%s, %s) '
        )
        data = ('Luiz', 18)
        result = cursor.execute(sql, data)
        # print(sql, data)
        # print(result)
    connection.commit()

    # inserindo um valor usadno placeholder e um dicionário
    with connection.cursor() as cursor:
        sql = (
            f'INSERT INTO {TABLE_NAME} '
            '(nome, idade) '
            'VALUES '
            '(%(name)s, %(age)s) '
        )
        data2 = ({
            "age": 37,
            "name": "Lo",})
        result = cursor.execute(sql, data2)
        # print(sql)
        # print(data2)
        # print(result)
    connection.commit()

    # Inserindo vários valores usando placeholder e uma tupla de dicionários
    with connection.cursor() as cursor:
        sql = (
            f'INSERT INTO {TABLE_NAME} '
            '(nome, idade) '
            'VALUES '
            '(%(name)s, %(age)s) '
        )
        data3 = (
            {"name": "Sah", "age": 27,},
            {"name": "Julia", "age": 74,},
            {"name": "Rose", "age": 54,},
        )
        result = cursor.executemany(sql, data3)
        # print(sql)
        # print(data3)
        # print(result)
    connection.commit()

    # Inseridno vários valores usando placeholder e uma tupla de tuplas
    with connection.cursor() as cursor:
        sql = (
            f'INSERT INTO {TABLE_NAME} '
            '(nome, idade) '
            'VALUES '
            '(%s, %s) '
        )
        data4 = (
            ("Siri", 22),
            ("Cortana", 15),
        )
        result = cursor.executemany(sql, data4)
        # print(sql)
        # print(data4)
        # print(result)
    connection.commit()

    # Lendo os valores com SELECT
    with connection.cursor() as cursor:
        # menor_id = input('Digite o menor id: ')
        # maior_id = input('Digite o maior id: ')
        menor_id = 2
        maior_id = 4
        coluna = 'id'
        sql = (
            f'SELECT * FROM {TABLE_NAME} '
            'WHERE id BETWEEN %s AND %s '
        )
        cursor.execute(sql, (menor_id, maior_id))
        # print(cursor.mogrify(sql, (menor_id, maior_id)))
        # data5 = cursor.fetchone()
        # print(data5)
        # for row in data5:
        #     print(row)
        
        data5 = cursor.fetchall() # aqui ele esgota o iterator

    # Apagando com DELETE, WHERE e placeholders no PyMySQL
    # CUIDADO COMO 'DELETE' SEM 'WHERE' 
    with connection.cursor() as cursor:
        sql = (
            f'DELETE FROM {TABLE_NAME} '
            'WHERE id = %s '
            )
        print(cursor.execute(sql, (1,)))
        connection.commit()

        cursor.execute(f'SELECT * FROM {TABLE_NAME} ')
        # for row in cursor.fetchall():
        #     print(row)

    # Editando com UPDATE, WHERE  e placeholders no PyMySQL
    with connection.cursor() as cursor:
        sql = (
            f'UPDATE {TABLE_NAME} '
            'SET nome = %s, idade = %s '
            'WHERE id = %s '
            )
        cursor.execute(sql, ('Eleonor', 102, 4))

        cursor.execute(f'SELECT * FROM {TABLE_NAME} ')

        for row in cursor.fetchall():
            print(row)
        connection.commit()
