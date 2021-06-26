# Numbers

print(2 + 1)                # addition
print(2 - 1)                # subtraction
print(4 ** 2)               # power of
print( 2+10 * 10+3)         # <--- will not work correctly, PEMDAS works as expected
print( (2+10) * (10+3))     # Parantheses to specify order of operations

# Variables
# Python doesn't need explicit type declaration for variables

a = 5                       # declaration and definition of variable
print(a)                    # print variable
print(a + a)                # arithmetic with variables
a = a * 5                   # python supports reassignment
print(a)                    # print result

# Variable rules

### Can't start with a number | any of these symbols: !@#$^&)(*)

# More Variables

my_income = 100
tax_rate = 0.1
my_taxes = my_income * tax_rate         # Python implicitly converts numbers to floating point if floating point exists in expression
print(my_taxes)