# How does python know something is string? --> By Quotes.
"Hello"             # This is a string because it is enclosed in quotes.
# Hello             # This is not a string because it is not enclosed in quotes.
#name = Ujjwal      # This will give an error because Ujjwal is not enclosed in quotes.


# Types of quotes in Python:
# 1. Single Quotes
'Hello'             # This is a string because it is enclosed in single quotes.
# 2. Double Quotes 
"Hello"             # This is a string because it is enclosed in double quotes.
# 3. Triple Quotes  #Used for multi-line strings or docstrings.
'''Hello'''         # This is a string because it is enclosed in triple quotes.
print("""Hello!
This is python""")         # This is a string because it is enclosed in triple quotes.


# What string can contain?
# A string can contain letters, numbers, spaces, and special characters.
"Hello World!"     # String with literal, 
"12345"            # This is a string because it is enclosed in quotes and contains numbers
"!@#$%^&*()_+{}[]" # This is a string because it is enclosed in quotes and contains letters, numbers, and a special character.
# String can also contain escape characters.
"\n \t"    # This is a string because it is enclosed in quotes and contains an escape character (\n) which represents a new line.
""                 # This is an empty string.


# If single quotes are used to define a string, then double quotes can be used inside the string and vice versa.
'This is a string with "double quotes" inside it.'
"This is a string with 'single quotes' inside it."
# "This is a string with "Double quotes" inside it."   # Error
# To include the same type of quote inside a string, we can use the escape character (\).
print(1, "\tThis is a string with \"double quotes\" inside it.")
print(2, "\tThis is a string with \'single quotes\' inside it.") 
print(3, "\tThis is Ujjwal\'s pen.")