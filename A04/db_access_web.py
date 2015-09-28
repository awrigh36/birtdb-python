import cgitb

import request


cgitb.enable()
import db_access


def send_request(stmt):
    url = 'http://127.0.0.1/cgi-bin/birt.py/'
    # response = urllib2.urlopen(url).read()
    request_path = url + stmt
    request.request_to_birt(request_path)


def get_all_customers():
    return db_access.get_all_customers()


def get_all_payments_for_customer(cust_num):
    return db_access.get_all_payments_for_customer(str(cust_num))


def get_all_orders_for_customer(cust_num):
    return db_access.get_all_orders_for_customer(str(cust_num))


def get_all_order_details_for_order(order_num):
    return db_access.get_all_order_details_for_order(order_num)