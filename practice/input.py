# name = input("What is your name?: ")
# age = input("What is your age?:")
# print(f"Hello {name}, you are {age} years young")

# num1 = float(input('Enter a digit: '))
# num2 = float(input('Enter a second number:'))
# answer = num1 * num2
# print(answer)


user = input("What is your name?: ")
dist_km = float(input("How far did you run in kms?: "))
km_to_miles = float((dist_km / 1.609))

print(f"""Hey {user.capitalize()}, conrats on running {dist_km}kms. 
Did you realise that is {round(km_to_miles,1)} in miles""")

#Round will round the number