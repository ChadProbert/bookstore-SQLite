""" Overview of the program:
Creates a database table and performs database manipulation queries on it.
"""

import sqlite3

try:
    # connection to db
    db = sqlite3.connect("./db/d")
    cursor = db.cursor()

    # create table if it doesn't exist
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS
    python_programming(id INTEGER NOT NULL UNIQUE PRIMARY KEY, name TEXT, grade
    INTEGER)"""
    )

    # commit changes to the database
    db.commit()
    print("Table created")

    # clear table before inserting the student data so that there
    # isn't duplicate data if the program is run multiple times
    cursor.execute("""DELETE FROM python_programming""")

    # insert data into table
    cursor.executemany(
        """INSERT INTO python_programming (id, name, grade)
    VALUES(?,?,?)""",
        [
            (55, "Carl Davis", 61),
            (66, "Dennis Fredrickson", 88),
            (77, "Jane Richards", 78),
            (12, "Peyton Sawyer", 45),
            (2, "Lucas Brooke", 99),
        ],
    )
    print("Student data inserted \n")

    # save changes to the database
    db.commit()

    # select all records with a grade between 60 and 80
    cursor.execute("""SELECT * FROM python_programming WHERE grade BETWEEN 60 AND 80""")
    print("Students with grades between 60 and 80")
    for row in cursor:
        print(row)

    # change Carl Davis' grade to 65
    cursor.execute(
        """UPDATE python_programming SET grade = 65 WHERE name = 'Carl Davis'"""
    )
    print("\nCarl Davis grade updated to 65")

    db.commit()

    # delete Dennis Fredrickson row
    cursor.execute(
        """DELETE FROM python_programming WHERE name = 'Dennis Fredrickson'"""
    )
    print("Dennis Fredrickson deleted")

    db.commit()

    # change the grade of all students with an id greater than 50 to 80
    cursor.execute("""UPDATE python_programming SET grade = 80 WHERE id > 50""")
    print("Students with id greater than 50 updated to 80 \n")

    db.commit()

    # display all records after the changes have been made
    cursor.execute("""SELECT * FROM python_programming""")
    print("Db table after changes: ")
    for row in cursor:
        print(row)

# catch errors and revert changes
except Exception as e:
    db.rollback()
    raise e

finally:
    # close connection to db
    db.close()
    print("\nConnection closed")


# References:
# This task's PDF file and and code files
