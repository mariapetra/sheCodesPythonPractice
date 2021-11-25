msg ='Welcome to Python 101: Split and Join'
csv = 'Eric,John,Michael,Terry,Graham'
friends_list = ['Eric','John','Michael','Terry','Graham']
print(msg.split())

# prints / ['Welcome', 'to', 'Python', '101:', 'Split', 'and', 'Join']
#type = list
#you can enter the data at which point you want it to split:

print(csv.split(','))
#prints // ['Eric', 'John', 'Michael', 'Terry', 'Graham']

print(' '.join(friends_list))
#if you turn this to a string it prints everything seperately like a list so to avoid this use join - the character that you put into your '' wull be inbetween the data
#can concatenate by adding another variable

#split = list / join = string

print(msg.replace('e', 'zz')) #replace first data with second