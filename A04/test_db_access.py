from db_access_web import get_all_customers, get_all_payments_for_customer, get_all_orders_for_customer
from db_access_web import get_all_order_details_for_order


def all_cust():
    customers = get_all_customers()
    #print(customers)
    #print(len(customers))
    if len(customers) == 122:
        print('all customers passed')
    else:
        print('all customers failed****************')


def all_payments():
    cust_num = 103
    payments = get_all_payments_for_customer(cust_num)
    max = 0
    for p in payments:
       # print(p)
        if p['amount'] > max:
            max = p['amount']
    if len(payments) == 3:
        print("payments passed")
    else:
        print("payments failed****************")
    if max == 14571.44:
        print("payments passed")
    else:
        print("payments failed****************")


def all_orders():
    cust_num = 103
    orders = get_all_orders_for_customer(cust_num)
    max = 0
    for ord in orders:
        #print(ord)
        if max < ord['orderNumber']:
            max = ord['orderNumber']
    if len(orders) == 3:
        print("orders passed")
    else:
        print("orders failed****************")
    if max == 10345:
        print("orders passed")
    else:
        print("orders failed****************")


def all_order_details(order_num):
    ord_det = get_all_order_details_for_order(order_num)
    min = 9999999
    for od in ord_det:
        #print(od)
        if min > od['priceEach']:
            min = od['priceEach']
    if len(ord_det) == 4:
        print("details passed")
    else:
        print("details failed")
    if min == 43.27:
        print("details passed")
    else:
        print("details failed")


if __name__ == "__main__":
    all_cust()
    all_payments()
    #print('='*50)
    all_orders()
    #print('='*50)
    all_order_details(10123)