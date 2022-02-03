"""The program should go through the customer orders file and find customers who didn't pay what was expected. The output should be formatted in this manner: 
Sean paid $9.50, expected $9.00
Ashley paid $2.00, expected $3.00"""

#state how much a melon costs
MELON_COST = 1.00

#create function
def find_pay_differences(customer_orders):
    
    
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
