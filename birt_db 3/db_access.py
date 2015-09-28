#!/user/bin/python


import mysql.connector
from mysql.connector import errorcode

try:
    cnx = mysql.connector.connect(user='root', password='dbapp',
                                  host='localhost',
                                  database='birt')
    cursor = cnx.cursor()

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Incorrect username/password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)


def get_all_customers():
    cursor0 = cnx.cursor()
    query = "SELECT * FROM customers"
    response = 0
    try:
        it = cursor0.execute(query, multi=True)
        row = cursor0.fetchone()
        while row in it is not None:
            for i in row:
                response = tuple(row[i])
            row = cursor0.fetchone()

    except ValueError as ve:
        response = 'E'

    return response


def get_all_payments_for_customer(cust_num):
    cursor1 = cnx.cursor()
    response = 0
    query1 = 'SELECT * FROM payments WHERE customerNumber = %s'
    try:
        it = cursor1.execute(query1, (cust_num + '',), multi=True)
        for x in it:
            response = x.fetchall()

    except ValueError as ve:
        response = 'ECustomer id should be a valid integer'

    cursor1.close()

    return response


def get_all_orders_for_customer(cust_num):
    cursor2 = cnx.cursor()
    query2 = "SELECT * FROM orders WHERE customerNumber = %s"
    try:
        it = cursor2.execute(query2, (str(cust_num) + '',), multi=True)
        for x in it:
            response = x.fetchall()

    except ValueError as ve:
        response = 'ECustomer id should be a valid integer'

    cursor2.close()

    return response


def get_all_order_details_for_order(order_num):
    cursor3 = cnx.cursor()
    query3 = "SELECT * FROM orderDetails WHERE orderNumber = %s"
    try:
        it = cursor3.execute(query3, str(order_num) + '',)
        for x in it:
            response = x.fetchall()

    except ValueError as ve:
        response = 'ECustomer id should be a valid integer'

    cursor3.close()

    return response