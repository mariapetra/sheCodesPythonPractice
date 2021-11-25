# sets use curly brackets
#cannot have duplicates / removes duplicates / unordered

#Sets - blazingly fast unordered Lists 
friends = ['John','Michael','Terry','Eric','Graham']
friends_tuple = ('John','Michael','Terry','Eric','Graham')
friends_set = {'John','Michael','Terry','Eric','Graham','Eric'} #would remove the last Eric
my_friends_set = {'Reg','Loretta','Colin','Eric','Graham'}

print(friends)
print(friends_tuple)
print(friends_set)

# ['John', 'Michael', 'Terry', 'Eric', 'Graham']
# ›('John', 'Michael', 'Terry', 'Eric', 'Graham')
# ›{'John', 'Michael', 'Terry', 'Eric', 'Graham'}

print(friends_set.intersection(my_friends_set))
# {'Eric', 'Graham'}
# # shows you the data that exists in both sets
print(friends_set.difference(my_friends_set))
#shows all different
print(friends_set.union(my_friends_set))
#will join

#how to set these data types as empty
#empty Lists
empty_list = []
empyt_list = list()

#empty Tuple
empty_tuple = ()
empty_tuple = tuple()

#empty Set
empty_set = {} # this is wrong, this is a dictionary
empty_set = set()
old_friends = {"joe", "stacey"}
new_friends = {"dave", "chloe"}
print(old_friends | new_friends) #this joins sets only
print(old_friends & new_friends) #in both sets
print(old_friends - new_friends) #confusing... not sure



