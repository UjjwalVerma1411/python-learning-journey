# String Operations

# Concatenation - Joining two string.
print("1\t", "Hello" + "World")
print("2\t", "Hello" + " World")
x, y = "Ujjwal", "Verma"
print("3\t", x + " " + y)
#print("Hello" + 2)


# Repetition (*) = Repeate the string int times.
print("4\t", "Hi" * 5)     # Spaces are not added automatically
print("5\t", "Hi " * 5)
a = "Hi"
print("6\t", a * 5)
print("7\t", a * 0)        # Empty String
print("8\t", a * -1)       # Negative Repetition is treated as 0 repetion 
#print("hi" * 2.5)          # Passing float value - Kuch sense hai iss bath ka.


# Membership Operator :Membership checks whether a value exists inside another object.
# 2 Types -> In Operator and Not Operator
py = "Python"
# In Operator
print("9\t",  "Pyt" in "Python")
print("10\t",  "ty" in "Python")    # Order is imp.
print("11\t", "on" in py)
print("12\t", "p" in py)
print("13\t", "z" in py)
print("14\t", "" in py)
# Not In
py = "Python"
print("15\t",  "Pyt" not in "Python")
print("16\t",  "ty" not in "Python")    # Order is imp.
print("17\t", "on" not in py)
print("18\t", "p" not in py)           # Case sensitive
print("19\t", "z" not in py)
print("20\t", "" not in py)