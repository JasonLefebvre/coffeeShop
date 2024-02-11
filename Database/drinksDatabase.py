import sqlite3

drinks = sqlite3.connect('drinks.db')

cursorDrinks = drinks.cursor()
cursorDrinks.execute("""
CREATE TABLE IF NOT EXISTS drinks(
    id INTEGER,
    name TEXT,
    price INTEGER
)
""")

drinks.commit()

drinks.close()