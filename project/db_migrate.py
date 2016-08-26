from views import db
from _config import DATABASE_PATH
import sqlite3
from datetime import datetime

# with sqlite3.connect(DATABASE_PATH) as connection:
    #
    # Get a cursor
    #
    # c = connection.cursor()
    #
    # Temporarily alter the name of the tasks table
    #
    # c.execute("""ALTER TABLE tasks RENAME TO old_tasks""")
    #
    # Recreate a new tasks table with the updated schema
    #
    # db.create_all()
    #
    # Retrieve the data from the original table
    #
    # c.execute("""SELECT name, due_date, priority, status FROM old_tasks ORDER BY task_id ASC""")
    #
    # Save all rows as a list of tuples; set posted_date to now and user_id to 1
    #
    # data = [(row[0], row[1], row[2], row[3], datetime.now(), 1) for row in c.fetchall()]
    #
    # Insert data into tasks table
    #
    # c.executemany("""INSERT INTO tasks (name, due_date, priority, status, posted_date, user_id)
    #                  VALUES (?, ?, ?, ?, ?, ?)""", data)
    #
    # Delete old_tasks table
    #
    # c.execute("""DROP TABLE old_tasks""")

with sqlite3.connect(DATABASE_PATH) as connection:
    c = connection.cursor()
    c.execute("""ALTER TABLE users RENAME TO old_users""")
    db.create_all()
    c.execute("""SELECT name, email, password
                 FROM old_users
                 ORDER BY id ASC""")
    data = [(row[0], row[1], row[2], 'user') for row in c.fetchall()]
    c.executemany("""INSERT INTO users (name, email, password, role)
                     VALUES (?, ?, ?, ?)""", data)
    c.execute("DROP TABLE old_users")
