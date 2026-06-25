# Immutable
py = "Python"
#py[0] = "J"       # TypeError: 'str' object does not support item assignment
py = "Jython"     # Reassignment of variable. New variable is created and name is refered to it.

# Example 2
py = "Python"
py = py + "World"
print(py)

# Example 3
a = "alan"
print(a.upper())
print(a)