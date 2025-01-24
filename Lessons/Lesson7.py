import sqlite3

# A4 бумага
db = sqlite3.connect("Users.db")
# Это наша рука с ручкой
cursor = db.cursor()


def create_table():
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users(
            name VARCHAR (20) NOT NULL,
            age INTEGER NOT NULL,
            hoby TEXT
        )
                   """)
    db.commit()


create_table()


# CRUD - Созданые - Чтение - Обновление - Удаление

def add_user(name, age, hoby):
    cursor.execute(
        'INSERT INTO users(name, age, hoby) VALUES (?,?,?)',
        (name, age, hoby)
    )
    db.commit()
    print(f"Добавили {name}")


add_user("Ardager", 26, "спать")

db.close()