################ Errors and Exceptions

# We can use Try, Except, and Finally keywords to handle situations in the case of an error

# We will use the file reading and writing methods in Python to show how this works.

###############
# Error Types #
###############

# print('hello)  <----- If we ran this, it would return a SyntaxError because we had an error in the syntax

# mylisthere = [1, 2, 3]
# print(mylist)  <----- This would return a NameError, because 'mylist' is not defined

## The point here is, these two error types are there to help us identify what kind of error we are dealing
## with.  In fact, these 'error types' are actually called exceptions.

#############################
# Exception Handling Syntax #
#############################

# Below is an example of how exception handlingn would be coded using the try, except, finally keywords.

# try:
#   You do your operations here...
#   ...
#   except ExceptionI:
#       If there is ExceptionI, then execute this block
#   except ExceptionII:
#       If there is ExceptionII, then execute this block.
#       ...
#   else:
#       ..., etc.

# Above, we would replace ExceptionI and ExceptionII with an exception type, like the ones described
# before: SyntaxError and NameError

# Example using the file manipulation functions of Python:

# open(): open a file, either read or write it, and then close it

# This code below will break the program with an exception
# f = open('simple.txt', 'r')
# f.write("Test write to simple text!")
# print("Hello world")

# But below we can fix the issue by addressing what happens when the error comes up
try:
    f = open('simple.txt', 'w')                 # 'r' for read, 'w' for write
    # they're important because 'r' gives you only reading permissions,
    # good to make sure that your code doesn't accidentally write over a file
    f.write("Test write to simple text!")
except IOError:
    print("ERROR: COULD NOT FIND FILE OR READ DATA!")
else:
    print("SUCCESS!")
    f.close()

# Exception handling is great, because we are addressing a potential error that would stop our code
# from running, but now that we've handling, we can proceed to our next code:
print("Hello world")

########################################################
# How do I know what type of error is going to happen? #
########################################################

# If you don't know what type of error you need to address, we don't necessarily need the exception type.

# except:

# Excluding the type will address a situation where -any- error comes up at all.

###################
# Finally keyword #
###################

# The finally keyword allows our code to run regardless of there being an error found

try:
    f = open('simple.txt', 'w') 
    f.write("Test write to simple text!")
except IOError:
    print("ERROR: COULD NOT FIND FILE OR READ DATA!")
# notice that before we had an 'else' block, and we replaced it with 'finally'
finally:
    print("I ALWAYS WORK NO MATTER WHAT!")
    f.close()

###############
# SyntaxError #
###############

# SyntaxError is usually never used in exception handling, because if the error happens before it reaches
# an 'except' block, then the error happens anyway. Exception handling is usually only helpful for specific
# operations-related code to know why the issue happened - syntax errors will need to be addressed by the
# programmer manually.