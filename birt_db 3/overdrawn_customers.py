import db_access

cust = db_access.get_all_customers()
for value in cust:
    cust_num = cust[1]
    cust_fname = cust[2]
    cust_lname = cust[3]
    payments = cust[4]
    orders = cust[5]
    credit_limit = cust[6]
    if (credit_limit > 0
        and payments is not None
        and orders is not None):
        available_credit = float(str(credit_limit)) + float(str(payments)) - float(str(orders))

fmt = "{0:<5} {1:<20} {2:<20} {3:<10} {4:<10} {5:<10} {6:<10}"

if credit_limit + payments < orders:
    formatted = fmt.format(cust_num, cust_fname, cust_lname, payments, orders, credit_limit, available_credit)
