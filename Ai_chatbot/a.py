import psycopg2
 
conn = None
try:
    conn = psycopg2.connect(
        dbname='aaaaaa', user='postgres',
        password='SHiva@9811', host='localhost', port='5432'
    )
    cur = conn.cursor()
 
    # (b) insert a new product
    cur.execute(
        'INSERT INTO Products (product_id, product_name, price, quantity) '
        'VALUES (%s, %s, %s, %s)',
        (101, 'Wireless Mouse', 799.00, 50)
    )
 
    # (c) query products priced above 100
    cur.execute('SELECT * FROM Products WHERE price > %s', (100,))
    rows = cur.fetchall()
    for row in rows:
        print(row)
 
    conn.commit()   # save the insert permanently
 
except psycopg2.Error as e:
    # (d) roll back on any failure and report the error
    if conn:
        conn.rollback()
    print('Database operation failed, changes rolled back:', e)
 
finally:
    if conn:
        cur.close()
        conn.close()
