import db_utility
import db_access

customer_info = {'customerNumber': 0, 'customerName': 1, 'contactLastName': 2,
                 'contactFirstName': 3, 'phone': 4, 'addressLine1': 5,
                 'addressLine2': 6, 'city': 7, 'state': 8, 'postalCode': 9,
                 'country': 10, 'salesRepEmployeeNumber': 11, 'creditLimit': 12}

total_payments = {'customerNumber': 0, 'checkNumber': 1, 'paymentDate': 2,
                  'amount': 3}

order = {'orderNumber': 0, 'orderDate': 1, 'requiredDate': 2, 'shippedDate': 3,
         'status': 3, 'comments': 5, 'customerNumber': 6}

order_details = {'orderNumber': 0, 'productCode': 1, 'quantityOrdered': 2,
                 'priceEach': 3, 'orderLineNumber': 4}

customer_info = db_access.get_all_customers()

while customer_info[row] is not None:
    for row in range(len(customer_info)):
            customer_number = row[0].format(row)
            customer_name = row[1].format(row)
            credit_limit = row[12].format(row)

            total_payments = db_utility.get_total_payments_for_customer(customer_number)

            total_orders = db_utility.get_total_orders_for_customer(customer_number)

            avail_credit = credit_limit + total_payments - total_orders

fmt = "{0:<10} {1:<20} {2:<10} {3:<10} {4:<20} {5:<20} "
cust_num = "CustNum"
cust_name = "Customer Name"
pay = "Payments"
ord = "Orders"
lim = "Credit Limit"
avail = "Available Credit"
print(fmt.format(cust_num, cust_name, pay, ord, lim, avail))

for row in customer_info:
    print(fmt.format(customer_number, customer_name, total_payments,
          total_orders, credit_limit, avail_credit))