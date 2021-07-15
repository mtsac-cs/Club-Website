############## Objected Oriented Programming 2
########### Notes taken are following the Python and Django Full Stack Web Developer Bootcamp on Udemy.com
########### URL: https://www.udemy.com/course/python-and-django-full-stack-web-developer-bootcamp/

class Sample():
    pass

x = Sample()
print(type(x))

# Let's start by adding attributes and methods to the object.
## Attributes: characteristics of an object
    # - Example: an attribute can be that a class Dog can breathe, swim, etc
## Methods: operations we can  perform on the object
    # - Example: a method can be an action like bark() that can return sound 'woof woof'

##############
# Attributes #
##############

class Dog():

    # For more general attributes, we create class object attributes.
    # These attributes are independent of user input and are true no matter what
    # the user wants.
    species = "Mammal"

    # To create attributes, we define them using self.name, but first we declare them
    # inside of a special function

    # Pass 'self', essentially says that the __init__ method refers to the class
    # object instance itself
    def __init__(self, breed, name):      

        # Notice after self, we pass a variable named breed.  This is telling Python that this is a REQUIRED
        # attribute when the object is first initialized
        self.breed = breed          # define self.breed = breed, needs to equal the passed value
        self.name = name            # attribute with name of dog

# if we don't pass our required attributes, an error will pop up
mydog = Dog(breed = "Lab", name = "Sammy")           
print(type(mydog))                  # class type = Dog
print(mydog.breed)            # This time, we can pass it our class attribute and get its value

# Example of another dog from the same class
otherdog = Dog(breed = "Huskie", name = "Doug")
# also, most likely you'll see passed class parameters like this:
otherdog = Dog("Huskie", "Doug")
print(otherdog.breed)
print(otherdog.name)
print(otherdog.species)         # prints the class object attribute

###########
# Methods #
###########

class Circle():

    pi = 3.14

    # Notice below we can get our parameter attributes a default value
    def __init__(self, radius = 1):
        self.radius = radius

    # our first method
    # note: the reason we pass self is that we are telling Python that this method is a function of the 
    # class Circle, and not just a free-flowing function.
    def area(self):
        # Don't forget to refer to attributes using self., and if we're referring to Class-level attributes,
        # we use the class name, so for pi it's Circle.pi
        return self.radius * self.radius * Circle.pi

    # Setter method to change the radius
    def set_radius(self, new_r):
        self.radius = new_r

myc = Circle()
print(myc.radius)           # prints '1'

myc = Circle(3)
print(myc.radius)
print(myc.area())           # runs our class method, area()

#########################
# Redefining Attributes #
#########################

# One way we can redefine attributes in Python is by calling them directly

myc.radius = 100
print(myc.area())           # now our area will use the new number

# However, maybe we prefer to create a method that lets us set the radius, for clarity.  See 
# the class code above and look for setRadius()

myc.set_radius(999)
print(myc.area())