import sqlite3

# This connects to a file named 'database.db'. 
# If the file doesn't exist yet, Python will automatically create it for you!
connection = sqlite3.connect('database.db')

# A cursor is like a digital pen that executes SQL commands for us
cursor = connection.cursor()

# Create the 'letters' table based on our blueprint
cursor.execute('''
CREATE TABLE IF NOT EXISTS letters (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    sender TEXT NOT NULL,
    recipient TEXT NOT NULL,
    content TEXT NOT NULL,
    color_theme TEXT NOT NULL,
    timestamp TEXT NOT NULL
)
''')

# Save (commit) the changes and close the connection safely
connection.commit()
connection.close()

print("Database and 'letters' table created successfully!")