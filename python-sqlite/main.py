import sqlite3


if __name__ == '__main__':
    # Connect to the database (or create it if it doesn't exist)
    conn = sqlite3.connect('example.db')

    # Create a cursor object
    cursor = conn.cursor()

    # Create a table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        age INTEGER NOT NULL
    )
    ''')

    # Insert some data
    cursor.execute('''
    INSERT INTO users (name, age)
    VALUES ('Alice', 30),
        ('Bob', 24),
        ('Charlie', 29)
    ''')

    # Commit the transaction
    conn.commit()

    # Retrieve data
    cursor.execute('SELECT * FROM users')
    rows = cursor.fetchall()

    # Print the data
    for row in rows:
        print(row)

    # Close the connection
    conn.close()

