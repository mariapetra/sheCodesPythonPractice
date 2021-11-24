# foods = ["banana", "orange", "apple", "pear", "cheese"]
# print(foods.index("orange")) #prints 1 (where is orange)
# print(foods.count("orange")) #prints 1 (how many times orange is there)
# calories = [100, 52, 17, 5, 73]

# foods.sort() #sort alphabetically
# foods.sort(reverse=True) #descending
# foods.reverse() #reverse the string as it is

# print(min(calories)) #lowest number or first alphabetically
# print(max(calories)) #highest number or first alphabetically
# print(sum(calories)) #total number // no str access

# foods.append("chocolate")
# foods.insert(1, "strawberry")
# foods[3] = "mango" #will change the list 
# foods.extend(calories) ##adds calories to foods
# print(foods)

# # foods.remove("banana")
# # foods.pop() #pops it so you can still use it in your progran
# # foods.pop(2) #pops specific place 
# # foods.clear() #empty list
# # del foods #completely removes your list - it is gone
# # del foods[2] #just delete 2 - be careful with del
# # print(foods)
# new_foods = foods
# new_foods_2 = foods.copy()
# # new_foods_3 = list(foods)
# #all will copy your list into a new one

#lemonade exercise
sales_w1 = [7,3,42,19,15,35,9]
sales_w2 = [12,4,26,10,7,28]
sales = []
days_worked = int(input("How much did you make today? "))
sales_w2.append(int(days_worked))
sales = sales_w1 + sales_w2
sales.sort()

worst_day = min(sales) * 1.5

best_day = max(sales) * 1.5

print(f"My worst day I earned {worst_day}")
print(f"My best day I earned {best_day}")
print(f"combined = {worst_day + best_day}")
# print(f"{sales} ")
