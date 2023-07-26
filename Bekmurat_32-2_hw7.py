import sqlite3

def create_connection(hw_db):
    connection = None
    try:
        connection = sqlite3.connect(hw_db)
    except sqlite3.Error as e:
        print(e)
    return connection

def create_table(conn,sql):
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
    except sqlite3.Error as e:
        print(e)

def insert_products(conn, products):
    sql = '''INSERT INTO products
    (product_title,price,quantity)
    VALUES (?,?,?)'''
    try:
        cursor = conn.cursor()
        cursor.execute(sql,products)
        conn.commit()
    except sqlite3.Error as e:
        print(e)

def change_the_quantity(conn, product):
    sql = '''UPDATE Products SET quantity = ? WHERE id = ?'''
    try:
        cursor = conn.cursor()
        cursor.execute(sql, product)
        conn.commit()

    except sqlite3.Error as e:
        print(e)

def change_the_price(conn, product):
    sql = '''UPDATE Products SET price = ? WHERE id = ?'''
    try:
        cursor = conn.cursor()
        cursor.execute(sql, product)
        conn.commit()

    except sqlite3.Error as e:
        print(e)

def delete_product(conn, id):
    sql = '''DELETE FROM Products WHERE id = ?'''
    try:
        cursor = conn.cursor()
        cursor.execute(sql, (id,))
        conn.commit()

    except sqlite3.Error as e:
        print(e)

def print_the_table(conn):
    sql = '''SELECT * FROM Products'''
    try:
        cursor = conn.cursor()
        cursor.execute(sql)

        rows_list = cursor.fetchall()
        for row in rows_list:
            print(row)

    except sqlite3.Error as e:
        print(e)

def price_up_to_100_som(conn):
    sql = '''SELECT product_title, price, quantity FROM Products WHERE price <= 100 AND quantity > 5'''
    try:
        cursor = conn.cursor()
        cursor.execute(sql)

        rows_list = cursor.fetchall()
        for row in rows_list:
            print(row)

    except sqlite3.Error as e:
        print(e)

def find_by_name(conn, product_title):
    sql = '''SELECT product_title, price, quantity FROM Products
             WHERE product_title LIKE ? '''
    try:
        cursor = conn.cursor()
        cursor.execute(sql, (product_title,))

        conn.commit()

        rows_list = cursor.fetchall()
        for row in rows_list:
            print(row)

    except sqlite3.Error as e:
        print(e)

sql_create_products = '''
CREATE TABLE products (
id INTEGER PRIMARY KEY AUTOINCREMENT,
product_title VARCHAR(200) NOT NULL,
price FLOAT(8,2) NOT NULL DEFAULT 0.0,
quantity INTEGER NOT NULL DEFAULT 0.0 )
'''

connection_to_db = create_connection('hw.db')
if connection_to_db is not None:
    print('Successfuly connected to DB!')


def add_table():
    insert_products(connection_to_db,('Wireless Headphones',49.99,25))
    insert_products(connection_to_db,('Smartwatch',99,10))
    insert_products(connection_to_db,('Portable Bluetooth Speaker',39,15))
    insert_products(connection_to_db,('Digital Camera',249,5))
    insert_products(connection_to_db,('Game Console',299,8))
    insert_products(connection_to_db,('Fitness Tracker',79,20))
    insert_products(connection_to_db,('Streaming Device',59,12))
    insert_products(connection_to_db,('Mouse Set',29,30))
    insert_products(connection_to_db,('External Hard Drive',89,18))
    insert_products(connection_to_db,('Product: Home Security Camera',119,7))
    insert_products(connection_to_db,('Portable Power Bank',24,9940))
    insert_products(connection_to_db,('Wireless Earbuds',79,22))
    insert_products(connection_to_db,('Laptop Backpack',39,35))
    insert_products(connection_to_db,('Smart Home Hub',149, 6))
    insert_products(connection_to_db,('Computer Monitor',199,14))
#create_table(connection_to_db,sql_create_products)
#create_table(connection_to_db, sql_create_products)
#add_table()
#change_the_quantity(connection_to_db, (879, 6))
#change_the_price(connection_to_db, (799, 9))
#delete_product(connection_to_db, (8))
#print_the_table(connection_to_db)
#price_up_to_100_som(connection_to_db)
#find_by_name(connection_to_db, ('Fitness Tracker'))
connection_to_db.close()
