"""Accounting program for initializing new customers and checking payments"""

# Creates customer class
class Customer:
    melon_cost = 1.00

    def __init__(self, name, melons, paid):
        self.name = name
        self.melons = melons
        self.paid = paid

    def __repr__(self):
        print(f"{self.name} ordered {self.melons} melons and paid {self.paid} dollars.")

    def calculate_expected(self):
        """Calculates expected payment
        
        Calculates expected payment by multiplying melon quantity by melon cost
        """
        self.expected_payment = self.melons * self.melon_cost
    def check_payment(self):
        """Checks to see if the customer paid the correct amount
        
        Compares expected payment to actual payment
        If customer paid incorrect amount, displays statement
        """
        if self.expected_payment != self.paid:
            print(f"{self.name} paid ${self.paid:.2f}, expected ${self.expected_payment:.2f}")

def process_order_log(order_log):
    """Processes order log for incorrect payments
    
    # Unpack each order and instantiate customer into customers list
    # Check customer list for incorrect payments
    """
    # Empty list of customers
    customers = []
    # Open order log file
    orders = open(order_log)
    # Loop through orders
    for order in orders:
        # Remove whitespace
        order = order.rstrip()
        # Tokenize each order
        tokens = order.split("|")
        # Unpack tokens
        num, name, melons, paid = tokens
        melons = float(melons)
        paid = float(paid)
        customers.append(Customer(name, melons, paid))
    
    # Loop through customers
    for customer in customers:
        # Calculate expected payment for given customer
        customer.calculate_expected()
        # Check payment for given customer
        customer.check_payment()

# Processes given order log
process_order_log("customer-orders.txt")


# OLD DUMB CODE

# melon_cost = 1.00

# customer1_name = "Joe"
# customer1_melons = 5
# customer1_paid = 5.00

# customer2_name = "Frank"
# customer2_melons = 6
# customer2_paid = 6.00

# customer3_name = "Sally"
# customer3_melons = 3
# customer3_paid = 3.00

# customer4_name = "Sean"
# customer4_melons = 9
# customer4_paid = 9.50

# customer5_name = "David"
# customer5_melons = 4
# customer5_paid = 4.00

# customer6_name = "Ashley"
# customer6_melons = 3
# customer6_paid = 2.00

# customer1_expected = customer1_melons * melon_cost
# if customer1_expected != customer1_paid:
#     print(f"{customer1_name} paid ${customer1_paid:.2f},",
#           f"expected ${customer1_expected:.2f}"
#           )

# customer2_expected = customer2_melons * melon_cost
# if customer2_expected != customer2_paid:
#     print(f"{customer2_name} paid ${customer2_paid:.2f},",
#           f"expected ${customer2_expected:.2f}"
#           )

# customer3_expected = customer3_melons * melon_cost
# if customer3_expected != customer3_paid:
#     print(f"{customer3_name} paid ${customer3_paid:.2f},",
#           f"expected ${customer3_expected:.2f}"
#           )

# customer4_expected = customer4_melons * melon_cost
# if customer4_expected != customer4_paid:
#     print(f"{customer4_name} paid ${customer4_paid:.2f},",
#           f"expected ${customer4_expected:.2f}"
#           )

# customer5_expected = customer5_melons * melon_cost
# if customer5_expected != customer5_paid:
#     print(f"{customer5_name} paid ${customer5_paid:.2f},",
#           f"expected ${customer5_expected:.2f}"
#           )

# customer6_expected = customer6_melons * melon_cost
# if customer6_expected != customer6_paid:
#     print(f"{customer6_name} paid ${customer6_paid:.2f},",
#           f"expected ${customer6_expected:.2f}"
#           )
