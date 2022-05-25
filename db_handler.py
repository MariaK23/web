import sqlite3 as sql

#создание БД
def create_db(path):
    connect = sql.connect(path)
    cursor = connect.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS logs_table(
            form TEXT
            result TEXT
        );
        """
    )
    connect.commit()
    connect.close()

# запись в БД
def write_db(path, data):
    with sql.connect(path) as connect:
        cursor = connect.cursor()
        cursor.execute(
            """
            INSERT INTO logs_table
            VALUES (?,?);
            """,
            data
        )
        connect.commit()

# чтение из БД
def read_db(path, data):
    with sql.connect(path) as connect:
        cursor = connect.cursor()
        cursor.execute(
            """
           SELECT * FROM log_table;
            """
        )
        return cursor.fetchall()

