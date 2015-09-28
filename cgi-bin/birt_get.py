import logging

from json_with_dates import dumps
from birt_db import db_access


def send_data(data):
    data_j = dumps(data)
    logging.debug("custJ " + str(data_j))
    lng = len(data_j)
    logging.debug("len " + str(lng))
    print("Content-Type: application/json; charset=UTF-8")
    print("Content-Length: " + str(lng))
    print()
    print(data_j)


def all_customers():
    data = db_access.get_all_customers()
    send_data(data)


def total_payments_by_customer(path):
    id = path['match'].group(1)
    data = db_access.get_all_payments_for_customer(id)
    send_data(data)


def all_orders_by_customer(path):
    id = path['match'].group(1)
    data = db_access.get_all_orders_for_customer(id)
    send_data(data)


def all_order_details(path):
    id = path['match'].group(1)
    data = db_access.get_all_order_details_for_order(id)
    send_data(data)


def no_match(info):
    message = "Path " + info["path"] + " not found"
    print("Status: 404 Not Found")
    print("Content-Type: plain/text; charset=UTF-8")
    print("Content-Length: " + str(len(message)))
    print()
    print(message)


dispatch_get = [
    (r'/customer$', all_customers),
    (r'/customer/(\d+)/payments$', total_payments_by_customer),
    (r'/customer/(\d+)/orders$', all_orders_by_customer),
    (r'/order/(\d+)/details$', all_order_details),
    (r'', no_match),
]