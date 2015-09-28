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

cust = db_access_web.get_all_customers()

for row in cust:
    cust_number = row["customerNumber"]
    customer_name = row["customerName"]
    credit_limit = float(row["creditLimit"])

    total_payments = float(db_utility.get_total_payments_for_customer(cust_number))
    total_orders = float(db_utility.get_total_orders_for_customer(cust_number))

    available_credit = credit_limit + total_payments - total_orders

    if available_credit < 0:
        print(fmt.format(cust_number, customer_name, total_payments, total_orders, credit_limit, available_credit))