"""
one problem has been given :

Alogorithm for that problem
----------

steps to solve a problem :
step 1: Get the cost of items into variables
step 2: Get the quantity of items into variables
step 3: compute the selling price to each item,
        and add them
step 4: compute the subsidy amount and subtract
        from the selling price
step 5: Display the Billable amount

"""

# cost of Items
cost_of_wheat = 25
cost_of_rice = 12

#Quantities of Items
qty_of_wheat = 30 #kgs
qty_of_rice = 50

#Selling Price Computation
sp_of_wheat = cost_of_wheat * qty_of_wheat
sp_of_rice = cost_of_rice * qty_of_rice

total_sp = sp_of_wheat + sp_of_rice
# print(total_sp)
print("Total selling price:", total_sp)

# subsidy calculation at 20% subsidy
subsidy_amount = (total_sp * 20) / 100 #PEMDAS
print("Subsidy Amount : ", subsidy_amount)

billable_amount = total_sp - subsidy_amount
print("Billable amount : ", billable_amount)