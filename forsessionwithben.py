# Q1) Below is a list of foods 
# and their prices per unit: 

# Ask the user - done
# how many units - done
# of each item - done
# they bought,  - done
# then output the 
# corresponding receipt.

# For the input below, 
# assume that the input is provided in the same order 
# as defined in the list above.

groceries = [
      ["Baby Spinach", 2.78],
      ["Hot Chocolate", 3.70],
      ["Crackers", 2.10],
      ["Bacon", 9.00],
      ["Carrots", 0.56],
      ["Oranges", 3.08]
]

username = "Izzy"
for item in groceries:
    item_description = item[1]
    user_input = int(input(f"Hi {username}, how many units of {item[0]} did you buy? "))
    price = user_input * item_description
    item.append(price)
for price in groceries:
    subtotal = 0
    item_cost = price[2]
    subtotal = price * item[0]
print(f"""===={username}'s Food Emporium"====



=========================================
{subtotal}
""")


# #  Getting stuck on accessing the amount and outputing the total 
# #  getting - TypeError: 'int' object is not subscriptable
# # Also trying to do the sum and not able to as trying to add up
# # a list

# # prints:

# ====Izzy's Food Emporium"====
# [['Baby Spinach', 2.78, 2.78], ['Hot Chocolate', 3.7, 7.4], ['Crackers', 2.1, 2.1], ['Bacon', 9.0, 18.0], ['Carrots', 0.56, 0.56], ['Oranges', 3.08, 6.16]]


# =========================================


# Q4) Ask the user for a number and use this to generate 
# # a (different) pyramid of that height.

#1 *************** come back to************************

# Ask user for number:
#     need - user / input field / type int - asking for number
# Print pyramid:
#     Should say - Pyramid size:
#     (show Pyramind with character) *
#      Should iterarte through user input
#      Height (output) = user input 
#     Width input = empty string times user input + * times user input + empty string * user input
#     User input not predefined = while loop
# Three Loop Questions:
# 1. What do I want to repeat? - stars and spaces
#  -> 
# 2. What do I want to change each time? - the amount and the placement of stars and spaces
#  -> 
# 3. How long should we repeat? - until the users end point (length of input)
#  -> 

# user_input = int(input("Please enter a number: "))

# i = 0
# d = 0
# while i < user_input:
#     i += 1
#     d - 1
#     print( "*"*d)  
    
#  counter that goes up and a counter that goes down eg d that counts downs 
#    x d/ * i eg d -=1 for example
#Have tried indenting and adding code for " ". 
#Have tried duplicating the print statement

# Please enter a number: 5
# *
# **
# ***
# ****
# *****



