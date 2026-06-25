# String Function

# Length
print("===Length===")
py = "Python @12_3!#"
print(len(py))
print(len(""))
print(len("   "))
print(len("\t"))
last = len(py)-1
print("index: ", last, "\tElement: ", py[last])

# Ordinal Value - ord()
print("===Ordinal===")
print(ord("A"))
print(ord(" "))
#print(ord(""))     # Atleast One Element # TypeError: ord() expected a character, but string of length 0 found
#print(ord("12"))   # Atmost One Element  # TypeError: ord() expected a character, but string of length 2 found

# chr()
print("===chr===")
print(chr(65))
print(chr(48))
print(chr(64))
print(chr(32), "This is space.")      
#print(chr())     # Atleast One Element # TypeError: chr() takes exactly one argument (0 given)
#print(chr("65")) # Only Int allowed    # TypeError: 'str' object cannot be interpreted as an integer

# min()
print("===min===")
py = "Python"
print(min("Python"))
print(min("bacd"))
print(min(" abcs"))  # Space is smallest
print(min("2abcs"))
#print(min(""))      # Parameter must not be Empty.
print(min("\n"))     # 1st print \n and then move to next line
print(min("A"))

# max()
print("===max===")
py = "Python"
print(max("Python"))
print(max("bacd"))
print(max(" abcs"))  # Space is smallest
print(max("2abcs"))
#print(max(""))      # Parameter must not be Empty.
print(max("\n"))     # 1st print \n and then move to next line
print(max("A"))