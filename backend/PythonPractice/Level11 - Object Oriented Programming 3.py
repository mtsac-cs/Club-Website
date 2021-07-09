############## Objected Oriented Programming 3: Inheritance and Special Methods


# Inheritance: derived classes that inherit from parent (base) classes
# Special Methods: 

###############
# Inheritance #
###############

# Definition of a class that describes a generic animal
class Animal():

    def __init__(self):
        print("ANIMAL CREATED")

    def whoAmI(self):
        print("ANIMAL")

    def eat(self):
        print("EATING")

# Definition of a Dog that inherits from Animal

# Step 1: pass the base class (or parent class) into the definition of the Dog class
class Dog(Animal):

    def __init__(self):
        print("DOG CREATED")

    # Boom: created inherited class

    # Adding a unique method to the Dog class
    def bark(self):
        print("WOOF WOOF")

    # Overriding a method from the Animal class
    def eat(self):
        print("DOG EATING")

# This code demonstrates that our methods in Animal work
mya = Animal()
mya.whoAmI()
mya.eat()

# This code will show that our derived class, Dog, can call the same functions as Animal
myd = Dog()
myd.whoAmI()
myd.eat()
myd.bark()

###################
# Special Methods #
###################

class Book():
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    
    # Return a string when object is called as a string
    def __str__(self):
        return "Title: {}, Author: {}, Pages: {}".format(self.title, self.author, self.pages)
    
    # Instruct Python what to return if len() is used. Here we return the number of pages.
    def __len__(self):
        return self.pages

    # Print a message that object was deleted
    def __del__(self):
        print("A book was burned!")

# The problem with the code below is that when you print it,  we get a reference to the object,
# but we want a nicely-formatted string with our attributes.
b = Book("Python", "Jose", 200)
print(b)                # returns object reference

# To get our formatted string, we can use something called a special method, or various
# built-in helper methods you can use in classes.  In the class above, __str__ is one that
# lets us return a string when the objected is called as a string, for example when you pass it
# into print()

# Also note: this will typically be how the __str__ special method will be used.

print(b)                # prints formatted string

# Another special method is the __len__ method. It's already defined above, but if we were to 
# call the following code without it, it would return and say: TypeError: object of type 'Book' has no
# len()

print(len(b))           # TypeError: object of type 'Book' has no len()

# To fix this, we use the __len__ special method and return a number, any number. We want to return
# the number of pages.

print(len(b))           # returns 200

# There are many special methods in Python, and most you'll just learn and pick up on your own.
# Another useful one is called __del__, which runs when we delete our object.

b = Book("Python", "Jose", 200)     # Note: because we already defined b before, redefining it here also deletes the old b object
del b                   # Delete object and print string defined in class