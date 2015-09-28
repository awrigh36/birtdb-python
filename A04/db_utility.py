import db_access_web


def get_total_payments_for_customer(cust_num):
    total_payments = 0
    payments = db_access_web.get_all_payments_for_customer(cust_num)

    if payments is not None:
        for row in payments:
            pay = row['amount']
            total_payments += pay
    else:
        return 0
    return total_payments


def get_total_amount_for_order(order_num):
    total_amount = 0

    it = db_access_web.get_all_order_details_for_order(str(order_num))

    if it is not None:
        for row in it:
            quantity_ordered = row['quantityOrdered']
            price_each = row['priceEach']
            total_amount += float(quantity_ordered) * float(price_each)
    else:
        return 0

    return total_amount


def get_total_orders_for_customer(cust_num):
    total_orders = 0
    orders = db_access_web.get_all_orders_for_customer(cust_num)
    if orders is not None:
        for row in orders:
            total_orders += get_total_amount_for_order(row['orderNumber'])
    else:
        return 0

    return total_orders