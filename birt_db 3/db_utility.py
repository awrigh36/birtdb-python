import db_access


def get_total_payments_for_customer(cust_num):
    total_payments = 0
    cust_num_string = str(cust_num)
    it = db_access.get_all_payments_for_customer(cust_num_string)
    for x in it:
        amount = x[3]
        amount_str = str(amount)
        total_payments += float(amount_str)

    return str(total_payments)


def get_total_amount_for_order(order_num):
    it = db_access.get_all_order_details_for_order(order_num)
    quantity_ordered = it[2]
    price_each = it[3]
    total_amount = quantity_ordered * price_each

    return str(total_amount)


def get_total_orders_for_customer(cust_num):
    total_orders = 0
    it = db_access.get_all_orders_for_customer(cust_num)
    for x in it:
        total_orders + 1

    return str(total_orders)
