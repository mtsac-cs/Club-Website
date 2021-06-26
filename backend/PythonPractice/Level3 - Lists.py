# Lists

mylist = [1, 2, 3]              # list of numbers
mylist = ['string in here', 1, 2, 3, 4, True, 'asdf', [1, 2, 3]]            # we can have a list of multiple types of objects, even other lists
print(len(mylist))              # len() will tell you the length of a list

# Indexing
## Works just like strings

print(mylist[-1])               # prints last element

## Unlike strings, lists are mutable

print("Before reassignment: ")
print(mylist)
mylist[0] = 'NEW ITEM'
print("After reassignment: ")
print(mylist)

# Appending elements

mylist.append("NEW ITEM")
print(mylist)

## append() only adds one element at a time
mylist.append([1, 2, 3])        # this would only add one item as a list
print(mylist)

## use extend() to add multiple items
mylist.extend([4, 5, 6])        # extend must use another list to extend
print(mylist)

# Removing items from list

## pop() method
mylist = ['a', 'b', 'c', 'd', 'e']
item = mylist.pop()
print(mylist)                   # pop() removes last item and returns it (much like in assembly)
print(item)                     # this should contain 'e'

## strangely, we can also pop a specific element by a given index
item = mylist.pop(0)
print(item)                     # this will remove 'a' and return it

# reverse()

mylist = ['a', 'b', 'c', 'd', 'e']
mylist.reverse()
print(mylist)                   # reverses the order of the list

# sort()
mylist = [4, 6, 1, 7, 43, 2]    # sorts the list
mylist.sort()
print(mylist)

# nested lists

mylist = [1, 2, ['x', 'y', 'z']]
print(mylist[2][1])             # accessing a list within a list

# matrices
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

## list comprehension (more info in another lecture)
first_col = [row[0] for row in matrix]          # for loop that grabs the first element of every list
print(first_col)