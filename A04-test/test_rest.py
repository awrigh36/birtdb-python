__author__ = 'student'

from util import db_access_web

cust = db_access_web.get_all_customers()
print(cust)

print("="*50)

pmt = db_access_web.get_all_payments_for_customer(189)
print(pmt)

print("="*50)

ord = db_access_web.get_all_orders_for_customer(189)
print(ord)

print("="*50)

det = db_access_web.get_all_order_details_for_order(10297)
print(det)

print("="*50)