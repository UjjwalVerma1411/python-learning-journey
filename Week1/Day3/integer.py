# Integer are whole numbers without a decimal point. They can be positive, negative, or zero.
# In Python, there is no limit to the size of an integer, as long as you have enough memory to store it.

# Operations on integers include addition, subtraction, multiplication, division, modulus, exponentiation, and floor division.
print(3 + 2)
print(3 - 2)
print(3 * 2)
print(3 / 2)
print(3 % 2)
print(3 ** 2)
# It divides two numbers and rounds the result down to the nearest integer (toward negative infinity).
print(3 // 2)   # Output: 1
print(-3 // 2)  # Output: -2
print(3 // -2)  # Output: -2
print(-3 // -2) # Output: 1

print(3 // 2.0) # Output: 1.0
print(3.0 // 2) # Output: 1.0

print(7 / 3, "\t", 7 // 3)


# Number + Number is possible, but Number + String is not possible. It will give an error.
print(3 + 5)  # This will work
print(3 + 5.3)  # This will work

# print(3 + "Hello")  # This will raise a TypeError
# Solution - Type Casting: Convert the string to an integer before adding Or Integer to string
print(3 + int("5") , "\t This is a Integer")  # This will work
print(str(3) + "5" + "\t This is a string not an integer")    # This will work

print(str(3) + "hello" +  "\t This is a string not an integer")  # This will work
#print(3 + int("hello"))    # This will not work