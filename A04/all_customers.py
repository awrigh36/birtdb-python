import db_access_web
import db_utility

fmt = "{0:^10} {1:<35} {2:>15} {3:>15} {4:>20} {5:>20} "
cust_num = "CustNum"
cust_name = "Customer Name"
pay = "Payments"
ord = "Orders"
lim = "Credit Limit"
avail = "Available Credit"
print(fmt.format(cust_num, cust_name, pay, ord, lim, avail))

all_customers = db_access_web.get_all_customers()

for row in all_customers:
    customer_number = row["customerNumber"]
    customer_name = row["customerName"]
    credit_limit = row["creditLimit"]

    total_payments = db_utility.get_total_payments_for_customer(customer_number)
    total_orders = db_utility.get_total_orders_for_customer(customer_number)
    avail_credit = float(credit_limit) + float(total_payments) - float(total_orders)

    output = fmt.format(customer_number, customer_name, total_payments,
                        total_orders, credit_limit, avail_credit)

    print(output)