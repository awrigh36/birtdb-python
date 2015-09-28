import mysql.connector
from mysql.connector import errorcode
import cgitb
cgitb.enable()


def connection():
    cnx = mysql.connector.connect(user='dbapp', password='dbapp',
                                  host='localhost',
                                  database='birt')
    return cnx


def exec_cmd(cmd, args=[]):
    birt = connection()
    try:
        cursor = birt.cursor()
        cursor.execute(cmd, args)
        column_names = []
        for d in cursor.description:
            column_names.append(d[0])
        resp = [dict(zip(column_names, row)) for row in cursor]
        return resp

    finally:
        birt.close()


def get_all_customers():
    return exec_cmd("SELECT * FROM customers")


def get_all_payments_for_customer(cust_num):
    return exec_cmd("SELECT * FROM payments WHERE customerNumber = " + str(cust_num))


def get_all_orders_for_customer(cust_num):
    return exec_cmd("SELECT * FROM orders WHERE customerNumber = " + str(cust_num))


def get_all_order_details_for_order(order_num):
    return exec_cmd("SELECT * FROM orderDetails WHERE orderNumber = " + str(order_num))