import sqlite3

# 1. Create a database of students
with sqlite3.connect('students.db') as conn:
    cursor = conn.cursor()
    
    # 2. Create a table 'student' with the specified fields
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        hobby TEXT,
        name TEXT,
        surname TEXT,
        year_of_birth INTEGER,
        homework_points INTEGER
    )
    ''')

    # 3. Insert 10 students into the table
    students_data = [
        ('Reading', 'Ahah', 'LoL', 2000, 12),
        ('Swimming', 'Nazar', 'Tashtanov', 1999, 8),
        ('Painting', 'Donald', 'Trump', 2001, 15),
        ('Dancing', 'Kamala', 'Harris', 2000, 5),
        ('Running', 'Joe', 'Biden', 1998, 11),
        ('Singing', 'Askar', 'Akaev', 2002, 9),
        ('Gaming', 'Barack', 'Obama', 2000, 13),
        ('Cooking', 'Ronald', 'Reagan', 2001, 7),
        ('Writing', 'Tony', 'Stark', 1999, 14),
        ('Hiking', 'Vladimir', 'Putin', 1997, 6)
    ]

    cursor.executemany('''
    INSERT INTO students (hobby, name, surname, year_of_birth, homework_points)
    VALUES (?, ?, ?, ?, ?)
    ''', students_data)

    conn.commit()

    # 5. Read all students whose surname is longer than 10 characters

    cursor.execute('''
    SELECT * FROM students WHERE LENGTH(surname) > 10
    ''')
    students = cursor.fetchall()
    for student in students:
        print(student)

    print('-----------------------------------------------------------------------------')

    # 6. Change the names of all students whose homework points are more than 10 to 'genius'
    cursor.execute('''
    UPDATE students SET name = 'genius' WHERE homework_points > 10
    ''')
    conn.commit()

    # 7. Display all students named 'genius'

    cursor.execute('''
    SELECT * FROM students WHERE name = 'genius'
    ''')
    genius_students = cursor.fetchall()
    for student in genius_students:
        print(student)

    print('-----------------------------------------------------------------------------')


    # 8. Delete all students whose id is even
    cursor.execute('''
    DELETE FROM students WHERE id % 2 = 0
    ''')
    conn.commit()

    # Verify the remaining students

    cursor.execute('''
    SELECT * FROM students
    ''')
    remaining_students = cursor.fetchall()
    for student in remaining_students:
        print(student)
    print('-----------------------------------------------------------------------------')
