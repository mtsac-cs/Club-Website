########### Notes taken are following the Python and Django Full Stack Web Developer Bootcamp on Udemy.com
########### URL: https://www.udemy.com/course/python-and-django-full-stack-web-developer-bootcamp/

###################################
## Comparison Operators ###########
###################################

# Comparison Operators are the same as other languages like C++

############
# Equality #
############

1 == 1    # True
1 == "1"  # False

##############
# Inequality #
##############

1 != "1"  # True

################################################
# Operators are different than other languages #
################################################

# or ||

if (1 > 2) or (2 > 3) :
    print("Hello")
else :
    print("Bye")

# and &&

if (1 > 2) and (2 > 3) :
    print("Hello")
else :
    print("Bye")

########################################################
# Indentation is important!  No brackets = readability #
########################################################

if 1 < 2 :
    print('First block')
    if 20 > 3 :
        print("Second block")

##################
# Elif = else if #
##################

if (1 > 2) or (2 > 3) :
    print("Dog")
elif 3 == 3 :
    print("Cat!")
else :
    print("No cat")

#############
# For loops #
#############

## For loops with sequences

seq = [1, 2, 3, 4, 5, 6, 7]

# item could be named anything
for item in seq:
    # Code here
    print(item)

## For loops with dictionaries

d = {"Sam":1, "Frank":2, "Dan":3, "Sandra":4}

# Note: dictionaries will not always print in order
for item in d:
    print(item)         # to print values
    print(d[item])      # to print keys

## For loops and tuples

mypairs = [(1, 2), (3, 4), (5, 6)]

# this will print the pairs like (1, 2)
for item in mypairs:
    print(item)

# Tuple unpacking: printing out individual elements inside of the tuples
for (tup1, tup2) in mypairs:  # or without parantheses: for tup1, tup2 in mypairs:
    print(tup1)
    print(tup2)

###############
# While loops #
###############

i = 1

while i < 5:
    print("i is: {}".format(i))
    i = i + 1

#########
# Range #
#########

# Range is a function that returns an object with a given range of elements in a sequence
# Range is a generator: so it generates a list - saves memory

print(list(range(0, 3)))            # prints range from index 0 to 3
print(list(range(0, 3, 2)))         # third parameter is stepsize, so this will return only even numbers
# range(0, 10000000)                # this would return a list of that many numbers but we aint uncommenting that lol

# Range and for loops
for item in range(10):
    print(item)

##########################################
# List Apprehension: shorthand for loops #
##########################################


# for loops and 
x = [1, 2, 3, 4]
out = []
for num in x:
    out.append(num**2)

print(out)

# or even easier in shorthand:
out2 = [num**2 for num in x]
print(out2)