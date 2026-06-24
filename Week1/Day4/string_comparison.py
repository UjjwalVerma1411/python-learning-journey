# String Comparison
py = "Python"

print("===Equality operator===")
print("1\t", "Python" == py)
print("2\t", "Pyth" == py)
print("3\t", "python" == py)   # Case Sensitive
print("4\t", "Pyhton" == py)
print("5\t", "\tPython" == py) # Must be exactly same

print("===Not-Equal operator===")
print("1\t", "Python" != py)
print("2\t", "Pyth" != py)
print("3\t", "python" != py)   # Case Sensitive
print("4\t", "Pyhton" != py)
print("5\t", "\tPython" != py) # Must be exactly same

print("===Less Than (<) and Greater Than (>)===")
print("1\t", "Apple" > "Banana", "\t", "Apple" < "Banana")
print("2\t", "Car" > "Cat", "\t", "Car" < "Cat")
print("3\t", "abc" > "abcd", "\t", "abc" < "abcd")
print("4\t", "A" > "a", "\t", "A" < "a")
print("5\t", "Car" > "Cat", "\t", "Car" < "Cat")
print("6\t", "A" > " ", "\t", "A" < " ")
print("7\t", "a" > " ", "\t", "a" < " ")
print("8\t", "1" > " ", "\t", "1" < " ")
print("9\t", "0" > " ", "\t", "0" < " ")
print("10\t", "0" > "a", "\t", "0" < "a")
print("11\t", "0" > "A", "\t", "0" < "A")
print("12\t", "@" > "a", "\t", "@" < "a")
print("13\t", "100" > "20", "\t", "100" < "20")
print("14\t", "Apple" > "Apple", "\t", "Apple" < "Apple")


print("===Less Than or Equal to(<=) and Greater Than or Equal to (>=)===")
print("1\t", "Apple" > "Apple", "\t", "Apple" < "Apple")
print("2\t", "Apple" >= "Apple", "\t", "Apple" <= "Apple")
print("3\t", " " > "  ", "\t", " " < "  ")
print("4\t", "abc" > "abc ", "\t", "abc" < "abc ")
print("4\t", "a" > "", "\t", "a" < "")