# Tuples, Sets, and Booleans

## Tuples: are immutable sequences kind of like list, except you can't change values from the list
## Sets: are unordered collections of unique elements
## Booleans: true or false statements

# Booleans
## Booleans are capitalized: True, False

# Tuples
## Tuples are made just like you would a list, but you use parantheses instead of brackets:

t = (1, 2, 3)
print(t[0])                 # values are returned by index like in lists
t = ('a', True, 123)
print(t)

## Again, tuples are like lists, but are immutable
#t[0] = 'New'   <-   this would not work because you can't reassign values

# Sets
## unordered collections of unique elements

x = set()
x.add(1)
x.add(2)
print(x)

## again, sets are unordered, so every time we print a set, the order will be different

x.add(4)
x.add(4)
x.add(4)

## although the above will run, it won't actually add them to the set, because it only adds unique elements
print(x)

## a great technique taking advantage of this property is to convert a list with duplicate elements to a set, and it will remove duplicates
converted = set([1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 3])
print(converted)