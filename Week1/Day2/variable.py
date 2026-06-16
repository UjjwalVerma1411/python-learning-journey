# A variable is a name that refers (references) a value/object in memory.
# Variable must be associated with a value.
# Variable must be declared before it is used.
# If you try to use a variable before assigning it, Python raises a NameError.
x = 10
print(x)          # This will print 10 because x has been assigned a value.
#print(y)         # This will raise a NameError because y is not defined. 



# You can change the value of a variable in your program at any time, and Python will always keep track of its current value
x = 20
print(x, type(x))  # This will print <class 'int'> because x is an integer.
# You can also change the type of a variable by assigning a value of a different type to it.
x = 20.5
print(x, type(x))  # This will print 20.5 <class 'float'> because x is now an float.



# The value must be of the same type as the variable.
#z = int("Hello")  # This will raise a ValueError because "Hello" cannot be converted to an integer.
#print(z)          # This line will not be executed due to the error above.
z = int("10")      # This will work because "10" can be converted to an integer.
print(z)           # This will print 10 because "10" has been successfully converted to an integer.



# Chained Assignment is a feature in Python that allows you to assign the same value to multiple variables in a single line of code.
a = b = c = 5
print(a, b, c)  # This will print 5 5 5 because a, b, and c all refer to the same value 5.