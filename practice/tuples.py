#imutable lists - faster / more restrictive
#use regular parenthesis rather than square brackets
#cannot use append / pop / remove
#use for data you don't want to change

friends = ['John','Michael','Terry','Eric','Graham']
friends_tuple = ('John','Michael','Terry','Eric','Graham')
print(friends[2:4])
print(friends_tuple[2:4])

#prints
#['Terry', 'Eric']
# ('Terry', 'Eric')