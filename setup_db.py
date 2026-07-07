import sqlite3

connection = sqlite3.connect('students.db')

cursor = connection.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER NOT NULL,
        roll_number INTEGER UNIQUE NOT NULL
    )
''')

print("✅ Database aur Table successfully create ho gaye!")

connection.commit()
connection.close()