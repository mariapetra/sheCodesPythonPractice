#Practicing Python and Python Notes

# Basic Arithmitic

a=10
b=3
print('Addition : ', a + b)
print('Subtraction : ', a - b)
print('Multiplication : ', a * b)
print('Division (float) : ', a / b)
print('Division (floor) : ', a // b)
print('Modulus : ', a % b)
print('Exponent : ', a ** b)

# prints

# Addition : 13
# ›Subtraction : 7
# ›Multiplication : 30
# ›Division (float) : 3.3333333333333335
# ›Division (floor) : 3
# ›Modulus : 1
# ›Exponent : 1000

msg = "welcome to it's Python 101: Strings"
print(msg)
print(msg.upper())
print(msg.lower())
print(msg.capitalize())
print(msg.title())
print(len(msg)) #shows length
print(msg.count('o')) #shows how many instances of 'o' = 3
#slicing
print(msg[2:7]) # prints: lcome // or you can remove the first numver [:7] and prints from start

# prints:

# welcome to it's Python 101: Strings
# ›WELCOME TO IT'S PYTHON 101: STRINGS
# ›welcome to it's python 101: strings
# ›Welcome to it's python 101: strings
# ›Welcome To It'S Python 101: Strings

#exercise slicing strings
msg='welcome to Python 101: Strings'
name = "Tyler"
print(msg)

new_str = f"{msg[18]} {msg[:7]} {msg[-5:-1]} {msg[8:10]} {name}"
print(new_str.title())
print(new_str[::-1].upper()) #makes it go backwards

#prints
# welcome to Python 101: Strings
# ›1 Welcome Ring To Tyler
# ›RELYT OT GNIR EMOCLEW 1

msg_multi = """Dear Terry,,
You must cut down the mightiest 
tree in the forest with…
a herring! <3"""
 #prints multi line strings

print(msg.find('h')) #will find the location index of h //can look for words too

print(msg.replace('Python','Java')) #replaces Python with Java
#these are not mutable you must save it as a new variable

print('Python' in msg) #prints true
