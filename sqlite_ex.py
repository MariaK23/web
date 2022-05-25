# система управления базами данных

import sqlite3 as sql

# соединение с базой данных
conn = sql.connect("test.db")

# курсор - "панель управления" БД
cursor = conn.cursor()

#создание таблицы 
sql_cmd = "create table if not exists users(userid int primary key, fname text, lname text, age real, gender text);"
cursor.execute(sql_cmd)
conn.commit()

# запись данных
# одна строка
# sql_cmd = """
#     INSERT INTO users VALUES(?,?,?,?,?);
# """
#cursor.execute(sql_cmd,(0,"John", "Sherman", 24.5, "m"))
#conn.commit()

# много строк 
# my_users = [
#     (1, "Joe", "Floyd", 32.5, "m"),
#     (2, "Irene", "Walters", 21.0, "f"),
#     (3, "Lilia", "Selters", 26.5, "f")
#     ]

# cursor.executemany(sql_cmd, my_users)
# conn.commit()

# чтение данных
# sql_cmd = """
#     SELECT * FROM users
# """
# cursor.execute(sql_cmd)
# result = cursor.fetchall()
# # result = cursor.fetchone()
# #result = cursor.fetchmany(3)
# print(result)

# чтение данных
# sql_cmd = """
# SELECT userid, fname, age FROM users WHERE age < 30 AND gender = "f";
# """
#cursor.execute(sql_cmd)
# result = cursor.fetchall()
# print(result)

# удаление данных
# sql_cmd = """
#    DELETE FROM users WHERE fname= "Sherman";
#"""
#cursor.execute(sql_cmd)
#result = cursor.fetchall()
#print(result)

# создание второй таблицы
# sql_cmd = """
#     CREATE TABLE IF NOT EXISTS orders
#     (
#         orderid INT PRIMARY KEY,
#         date TEXT,
#         userid TEXT,
#         total TEXT
#    );
# """

# cursor.execute(sql_cmd)
# conn.commit()

# запись данных во вторую страницу
# sql_cmd = """
#     INSERT INTO orders VALUES (?,?,?,?);
# """
# orders = [
#     (0, "23-05-2022", 2, "100"), 
#     (1, "23-05-2022", 2, "200"), 
#     (2, "24-05-2022", 1, "300"), 
#     (3, "25-05-2022", 3, "400"), 
#     (4, "26-05-2022", 1, "500"), 
# ]
# cursor.executemany(sql_cmd, orders)
# conn.commit()

# чтение данных со второй таблицы
# sql_cmd = """
# SELECT * FROM orders;
#  """
# cursor.execute(sql_cmd)
# result = cursor.fetchall()
# print(result)

#conn.close()

# извлечение данных из 2-х таблиц
# sql_cmd = """
#     SELECT * FROM orders LEFT JOIN users ON orders.userid = users.userid;
# """
# cursor.execute(sql_cmd)
# result = cursor.fetchall()

# запись данных во вторую страницу
sql_cmd = """
    INSERT INTO orders VALUES (?,?,?,?);
"""
orders = [
    (5, "27-05-2022", 4, "10"), 
    (6, "28-05-2022", 5, "20") 
]
cursor.executemany(sql_cmd, orders)
conn.commit()

sql_cmd = """
     SELECT * FROM orders INNER JOIN users ON orders.userid = users.userid;
"""
cursor.execute(sql_cmd)
result = cursor.fetchall()
print(result)

conn.close()
