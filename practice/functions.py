def greeting(name, age): #means define / name is a parameter / can set defaults with#
    return f"Hello {name} my friend! You are {age}"

name = input("What is your name?: ")
age = input("How old are you?")
print(greeting(name, age)) #argument
# named notation
# # def greeting(name, age=28, color="red"):
#  #Greets user with “name” from “input box” and “age”, if unavailable, default age is used   
   
#    print(f"Hello {name.capitalize()}, you will be {age+1} next birthday!")
#    print(f"We hear you like the color {color.lower()}!")

# greeting(age=27, name="brian",color="Blue") //means you can add them in any order
#also more readable