# Libraries Included:
# Numpy, Scipy, Scikit, Pandas

# -----2_str-----
# There is a list of products.
# Any product has price and belongs to a certain category.
# Store the list of products in sqlite database then find the average price for each category.
# Example of the data:
# Indesit, Oven, 1200
# Ariston, Oven, 1500
# Samsung, Oven, 3000
# Indesit, Fridge, 2000
# Leibherr, Fridge, 3000
#
# Example of the result:
# Oven, 1900
# Fridge, 2500
import sqlite3


def create_db(con):
    db = sqlite3.connect(con)
    db.execute("""
            CREATE TABLE Products(
            Id INTEGER PRIMARY KEY,
            Producer VARCHAR(30),
            Category VARCHAR(30) NOT NULL,
            Price FLOAT NOT NULL
            )""")
    db.commit()
    # cursor.close()


def insert_product_to_db(con, args=()):
    db = sqlite3.connect(con)
    cursor = db.cursor()
    cursor.execute("""
    INSERT INTO Products
    VALUES (?, ?, ?, ?)""", args)
    db.commit()
    cursor.close()


def get_avg_price_of_category(con, args=()):
    db = sqlite3.connect(con)
    cursor = db.execute("""
        SELECT AVG(Price) FROM Products
        WHERE Category=?""", args)
    return cursor.fetchall()[0]


con = "products.sqllite"
create_db(con)
insert_product_to_db(con, (1, 'Indesit', 'Oven', 1200))
insert_product_to_db(con, (2, 'Ariston', 'Oven', 1500))
insert_product_to_db(con, (3, 'Samsung', 'Oven', 3000))
insert_product_to_db(con, (4, 'Indesit', 'Fridge', 2000))
insert_product_to_db(con, (5, 'Leibherr', 'Fridge', 3000))
print(get_avg_price_of_category(con, ('Oven',)))
print(get_avg_price_of_category(con, ('Fridge',)))
