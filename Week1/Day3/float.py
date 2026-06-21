# A float (floating-point number) is a numeric data type used to represent numbers with a fractional or decimal part.

# Operations on Float include addition, subtraction, multiplication, division, modulus, exponentiation, and floor division.
print(3.1 + 2.2)    # Addition
print(3.1 - 2.2)    # Subtraction
print(3.1 * 2.2)    # Multiplication
print(3.1 / 2.2)    # Division
print(3.1 % 2.2)    # Modulus
print(3.1 ** 2.2)   # Exponentiation
# It divides two numbers and rounds the result down to the nearest integer (toward negative infinity).
print(3.1 // 2.2)   # Output: 1.0
print(-3.1 // 2.2)  # Output: -2.0
print(3.1 // -2.2)  # Output: -2.0
print(-3.1 // -2.2) # Output: 1.0

print(3.1 // 2.2) # Output: 1.0
print(3.0 // 2.0) # Output: 1.0

print(7.0 / 3.0, "\t", 7.0 // 3.0)


# Number + Number is possible, but Number + String is not possible. It will give an error.
print(3.1 + 5.2)  # This will work
print(3.1 + 5.3)  # This will work

# print(3.1 + "Hello")  # This will raise a TypeError
# Solution - Type Casting: Convert the string to an integer before adding Or Integer to string
print(3.1 + float("5.2") , "\t This is a Float")  # This will work
print(str(3.1) + "5.2" + "\t This is a string not a float")    # This will work

print(str(3.1) + "hello" +  "\t This is a string not a float")  # This will work
#print(3.1 + float("hello"))    # This will not work