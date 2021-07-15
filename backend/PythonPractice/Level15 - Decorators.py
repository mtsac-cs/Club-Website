########### Decorators
########### Notes taken are following the Python and Django Full Stack Web Developer Bootcamp on Udemy.com
########### URL: https://www.udemy.com/course/python-and-django-full-stack-web-developer-bootcamp/

# Decorators: Functions that modify the functionality of another function.  Help make code shorter!
# - Used a lot in Python web frameworks like Django and Flask

##########
# global #
##########

s = "GLOBAL VARIABLE"

def func():
    global s            # tells python to use the global definition of the s variable
    s = 50              # this reassigns s in the global scope as well
    print(s)

func()                  # returns 50
print(s)                # accesses global variable s, also returns 50

##########################
# globals() and locals() #
##########################

# globals() returns a dictionary of all globals currently available
# locals() returns a dictionary of all local variables currently available

def callVars():
    mylocal = 10

    print(globals())      # returns all globals
    print(globals()['s']) # returns a specific global
    print(locals())       # returns all locals

callVars()

##########
# Labels #
##########

# We can create a new variable in Python and assign it the name of a function without the parantheses.
# Essentially, this creates a reference to the function itself so that we can call it under a new name.

def hellothere(name):
    return "Hello " + name

print(hellothere("Sam"))
newname = hellothere
print(newname("Jorge"))

####################
# Nested Functions #
####################

# It is possible in Python to create nested functions

# Begin parent function:
def hello(name="John"):
    print("THE HELLO() FUNCTION HAS BEEN RUN!")

    # Nested function 1:
    def greet():
        return "THIS STRING IS INSIDE GREET()"
    # Nested function 2:
    def  welcome():
        return "THIS STRING IS INSIDE WELCOME()"
    
    # Note: we only defined the nested functions, but we can't access them outside of the scope of the
    # hello() function. So we need to call them while inside of hello() for them to execute.
    print(greet())
    print(welcome())

    print("End of hello()")

hello()

################################
# Controlling nested functions #
################################

# We can set conditions inside of a parent function that when true, it they will return a specific
# function

# Begin parent function:
def hello2(name="John"):
    print("THE HELLO() FUNCTION HAS BEEN RUN!")

    # Nested function 1:
    def greet():
        return "THIS STRING IS INSIDE GREET()"
    # Nested function 2:
    def  welcome():
        return "THIS STRING IS INSIDE WELCOME()"
    
    if name == "John":
        return greet
    else:
        return welcome

x = hello2()            # we assign it to a variable because hello2() returns a function reference
print(x())
x = hello2("Sam")
print(x())

##################################
# Passing functions as arguments #
##################################

# Define a function
def hijohn():
    return "Hi John"

# Define our function that will accept a function as a parameter
def other(func):
    # Note: if we pass hijohn() to this function, it's basically func = hijohn
    print("HELLO")
    print(func())

other(hijohn)

##############
# Decorators #
##############

# In the previous example, we essentially created a decorator

# Create a pretend decorator function:
def new_decorator(func):
    # Create a wrapper
    def wrap_func():
        print("CODE HERE BEFORE EXECUTING FUNC")
        func()      # where the passed function will be called
        print("FUNC() HAS BEEN CALLED")
    return wrap_func

# The function that will be passed to decorator
@new_decorator
def func_needs_decorator():
    print("THIS FUNCTION IS IN NEED OF A DECORATOR")

# Create a label and assign it the returned decorator function, pass it our func_needs_decorator function
#func_needs_decorator = new_decorator(func_needs_decorator)

# Instead of the commented out code above, we can do and use the @ command above to link the decorator
# to the function we want:
func_needs_decorator()