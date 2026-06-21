# Boolean
x = True    # T in True must be capitalized.
y = False   # F in False must be capitalized.
print(1, "\t", type(x), type(y))
print(2, "\t", 5>3, "\t", 5<3)

# Capitalize the first letter of True and False, otherwise it will be treated as a variable name.
# print(true, false)  # This will raise a NameError because 'false' is not defined.

# Bool Operations - NOT, AND, OR
a = True
b = False
# NOT
print(3, "\t", not a, "\t", not b)  # NOT operator inverts the boolean value.
print(4, "\t", not True, "\t", not False)
# AND - is True if both operands are True, otherwise it is False.
print(5, "\t", True and True)
print(6, "\t", True and False)
print(7, "\t", False and True)
print(8, "\t", False and False)
# OR - is True if at least one of the operands is True, otherwise it is False.
print(9, "\t", True or True)
print(10, "\t", True or False)
print(11, "\t", False or True)
print(12, "\t", False or False)


# True and False are also treated as 1 and 0 respectively when used in arithmetic operations.
print(13, "\t", True + True)  # This will return 2
print(14, "\t", True + False) # This will return 1
print(15, "\t", False + False) # This will return 0
print(16, "\t", int(True), int(False))
print(17, "\t", float(True), float(False))
print(18, "\t", str(True), str(False))
print(19, "\t", bool(1), bool(0))
print(20, "\t", 3 + int(True) - int(False))  # This will return 4

# Python sometimes treats non-boolean values as booleans it is Truthy and Falsy.
# Truthy and Falsy values in Python:
# The following values are considered False in Python:
print(21, "\t", bool(0), bool(0.0), bool([]), bool({}), bool(None))  # All these are False
print(22, "\t", bool(1), bool(-1), bool(0.1), bool([1, 2]), bool({"key": "value"}))  # All these are True

print(23, "\t", bool("Hello"), bool(""))  # Non-empty strings are True, empty strings are False