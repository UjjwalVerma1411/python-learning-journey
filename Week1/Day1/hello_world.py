#Simple Hello World
print("Hello World!")
print(10+1)


#Multiple Arguments  -->  Argument are seperated by a comma.
print("Hello! are you roll no.", 2, "or",3, "say", True, "if yes", "say", False, "if no.")



#Print type of any variable/constant
print(type(10))
print(type("10"))
print(type(True))
print(type(10.1))



#Why we don't need quotes for printing int/float or other data type
#Because quotes tell Python that something is text (a string).
print(10)
print(1.11)
print(True)
print("10")      # Here 10 is a string not int.
print("1.11")    # Here 1.11 is a string not float.
print("True")    # Here True is a string not Boolean.



#Python automatically moves the cursor to the next line after printing. Meaning After each print another print will automacticlly be prnited on the next line.
#If we want to print another print statement on the same line then we have to use "end" parameter
#end controls what gets printed after the output of a print() statement. By default, it is a newline (\n).
print("Hello World 1")
print("Hello World 2")
#These thing are same meaning--> print(, end=/n) == print()
print("Hello World 1", end="/n")
print("Hello World 2")

print("Hello World 1", end="")
print("Hello World 2")

print("Hello World 1", end=" ")
print("Hello World 2")

print("Hello World 1", end="a")
print("Hello World 2")

print("Hello World 1", end=" 0000 ")
print("Hello World 2")



""""
#Error Analysis Start

#NameError: name 'prin' is not defined
prin("Hello World!")


#SyntaxError: Unmatched ')'
print"Hello World!")


#SyntaxError '(' was never closed
print("Hello World!"


#SyntaxError: Unterminated String Literal (Detected at line 1)
print(Hello World!")


#SyntaxError: Unterminated String Literal (Detected at line 1)
print("Hello World!)


#Grammatical Error
print("Herld!")


#NameError: here hello is treated as variable and hello is not defined in the file.
print(Hello)

#Error End   
"""
