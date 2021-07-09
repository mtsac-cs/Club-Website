########## Scope

# Python scope follows the LEGB rule: Local -> Enclosing function locals -> Global -> built-in

# L: Local - Names assigned in any way within a function (def or lambda) and not declared global in that function
# E: (EFLS) - Name in the local scope of any and all enclosing functions (def or lambda), from inner to outer
# G: Global (module) - Names assigned at the top-level of a modul file, or declared global in a def within the file
# B: Buil-in (Python) - Names preassigned in the built-in names module: open, range, SyntaxError,...

# Example 1:

x = 25
def my_func():
    x = 50
    return x

print(x)            # Will print 25
print(my_func())    # Will print 50 because it is returning the value from the function

# This is where it can get confusing:
my_func()
print(x)            # This will print 25 because x = 50 is limited to the scope of my_func()

# Example of LOCAL scope
# This happens when variables exist inside of a function (block of code)
lambda x: x**2

# Enclosing Function locals
# This happens when variables are declared inside of nested blocks (nested functions)

# In the below function, greet() defines a variable name = "Sammy" and creates a nested function
# that prints Hello + name
def greet():
    name = "Sammy"
    
    def hello():
        print("Hello " + name)

    hello()                     # Without this function, greet() does nothing, because hello()
                                # is outside of our scope

greet()                         # prints "Sammy Hello"

# Now let's add a global variable:
name = "This is a global name!"
def greet():
    #name = "Sammy"             # Comment out the local variable
    
    def hello():
        print("Hello " + name)  # Now, hello() prints the global variable as it's the next variable up in scope

    hello()            

greet()                         # prints "This is a global name!"         


# Built-in Level
## Things that are already built-in, like len
## We never want to redefine these

# len = 3 will not run

# Variable Scope levels
## All variables are assigned a scope level corresponding to the block they are declared in

