#######  Functions
########### Notes taken are following the Python and Django Full Stack Web Developer Bootcamp on Udemy.com
########### URL: https://www.udemy.com/course/python-and-django-full-stack-web-developer-bootcamp/

####################################
# Declaring and defining Functions #
####################################

def my_func(param1 = 'default'):
    print("My first Python function")

# calling a function:
my_func()

# using parameters in a string
def my_func(param1 = 'default'):
    print("My first Python function! {}".format(param1))

my_func()

#########################
# Documentation strings #
#########################

def my_func(param1 = "default"):
    """
    THIS IS THE DOCSTRING
    """
    print("My first Python function!")

##########
# return #
##########

# print 'hello' using print() function
def hello():
    print("hello")

hello()

# print 'hello using return value
def hello():
    return "hello"
result = hello()
print(result)

#####################################################
# Python as a dynamic language and parameters types #
#####################################################

# We assume that this will work, it will always add 2 and 3:
def addNum(num1, num2):
    return num1 + num2
result = addNum(2, 3)
print(result)

# However, what if the user passes other types?
# result = addNum("2", 3)
# print(result)           # this will return a TypeError

# We can update the function with a check:
def addNum(num1, num2):
    if type(num1) == type(num2) == type(10):
        return num1 + num2
    else:
        "Sorry! I only take integers."

#####################
# Lambda Expression #
#####################

###### filter()
# filter() will filter out values based on a boolean expression true or false
mylist = [1, 2, 3, 4, 5, 6, 7, 8]

# this function returns true if num is an even number, false if not
def even_bool(num):
    return num % 2 == 0

# here we use the filter function: param 1 is our function passed into filter, then the second is the sequence we want to filter
# note: filter as a function will go through each value in mylist and pass the value into even_bool
evens = filter(even_bool, mylist)

# return a list with just even numbers
print(list(evens))          # we need to cast it as a list because otherwise, evens on its own prints out the memory location, filter is just a generator

###### doing the same thing with a lambda expression aka anonymous function

evens = filter(lambda num: num % 2 == 0, mylist)
print(list(evens))

###########
# split() #
###########

# Returns a string as a list and can take in a delimiter
tweet = "Go Sports! #Sports"
result = tweet.split("#")[1]            # the [1] will return the hashtag we want, we get the whole list without it
print(result)

###############
# in operator #
###############

# If you want to know if an element exists inside a sequence, use the in operator

print('x' in [1, 2, 3])                 # this will print 'False'