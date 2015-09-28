import db_access_web


def get_total_payments_for_customer(cust_num):
    total_payments = 0
    cust_num_string = str(cust_num)

    it = db_access_web.get_all_payments_for_customer(cust_num_string)

    if it is not None:
        for i in it:
            amount = i[3]
            amount_str = str(amount)
            total_payments += float(amount_str)

    return str(total_payments)


def get_total_amount_for_order(order_num):
    total_amount = 0
    order_num_string = str(order_num)

    it = db_access_web.get_all_order_details_for_order(order_num_string)

    if it is not None:
        for row in it:
            quantity_ordered = row[2]
            price_each = row[3]
            total_amount = float(quantity_ordered) * float(price_each)

    return total_amount


def get_total_orders_for_customer(cust_num):
    total_orders = 0
    cust_num_string = str(cust_num)

    it = db_access_web.get_all_orders_for_customer(cust_num_string)

    if it is not None:
        for i in it:
            order_number = i[0]
            total_orders += float(get_total_amount_for_order(str(order_number)))

    return total_orders
