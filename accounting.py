"""The program should go through the customer orders file and find customers who overpaid or underpaid."""

#state how much a melon costs
MELON_COST = 1.00

#create function
def find_pay_differences(customer_orders):
    
    orders = open(customer_orders)
    
    #go though each line in the file
    for line in orders:
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
        expected_payment = melons_purchased * MELON_COST

        #find the customers who didn't pay what was expected and format as a sentence
        if expected_payment > payment:
            print(f"{first_name} underpaid for their melons. They paid ${payment:.2f},", f"and expected payment is ${expected_payment:.2f}.")
        elif expected_payment < payment:
            print(f"{first_name} overpaid for their melons. They paid ${payment:.2f},", f"and expected payment is ${expected_payment:.2f}.")
    orders.close()


find_pay_differences("customer-orders.txt")

