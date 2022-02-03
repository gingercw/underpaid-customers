"""The program should go through the customer orders file and find customers who didn't pay what was expected. The output should be formatted in this manner: 
Sean paid $9.50, expected $9.00
Ashley paid $2.00, expected $3.00"""



#create function
def find_pay_differences(customer_orders):
    #state how much a melon costs
    melon_cost = 1.00
    
    #go though each line in the file
    for line in customer_orders:
        #remove extra spaces and punctuation from line and make it a list
        line = line.rstrip()
        words = line.split("|")

        #get the first name of the customer
        full_name = words[1]
        split_name = full_name.split(" ")
        first_name = split_name[0]

        #identify how many melons were bought and how much was paid
        melons_purchased = float(words[2])
        payment = float(words[3])

        #calculate how much the customer should have paid
        expected_payment = melons_purchased * melon_cost

        #find the customers who didn't pay what was expected and format as a sentence
        if expected_payment != payment:
            print(f"{first_name} paid ${payment:.2f},", f"expected ${expected_payment:.2f}")
    

orders = open("customer-orders.txt")
find_pay_differences(orders)
orders.close()


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
