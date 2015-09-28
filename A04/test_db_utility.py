
from db_utility import get_total_amount_for_order, get_total_orders_for_customer, get_total_payments_for_customer


def try_total_payments(cust_num):
    total = get_total_payments_for_customer(cust_num)
    #print("payments for customer {} are {:.2f}".format(cust_num, total))
    return total


def try_total_of_order(order_num):
    total = get_total_amount_for_order(order_num)
    #print("Total of order {} is {:.2f}".format(order_num, total))
    return total


def try_total_order_cust(cust_num):
    total = get_total_orders_for_customer(cust_num)
    #print("Total orders for customer {} is {:.2f}".format(cust_num, total))
    return total


if __name__ == "__main__":
    if try_total_payments(125) == 0:
        print("passed")
    else:
        print("failed****************")
    if try_total_payments(129) == 66710.56:
        print("passed")
    else:
        print("failed****************")
    if try_total_payments(131) == 107639.94:
        print("passed")
    else:
        print("failed****************")

    if try_total_of_order(10123) == 14571.44:
        print("passed")
    else:
        print("failed****************",try_total_of_order(10123), 4571.44)

    if try_total_of_order(10298) == 6066.78:
        print("passed")
    else:
        print("failed****************",try_total_of_order(10298), 6066.78)

    if try_total_order_cust(125) == 0:
        print("passed")
    else:
        print("failed****************")
    if try_total_order_cust(129) == 66710.56:
        print("passed")
    else:
        print("failed****************")
    if try_total_order_cust(131) == 149085.15:
        print("passed")
    else:
        print("failed****************",try_total_order_cust(131), 149085.15 )




