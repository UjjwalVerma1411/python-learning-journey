x = "python"
print(x)

# Accessing characters in a string: string[index]
# Accessing index of a character in a string: string.index(character)
print("1\t\t","1st character:", x[0], "\tIndex:", x.index("p"))
print("2\t\t","2nd character:", x[1], "\tIndex:", x.index("y"))
print("3\t\t","3rd character:", x[2], "\tIndex:", x.index("t"))
print("4\t\t","4th character:", x[3], "\tIndex:", x.index("h"))
print("5\t\t","5th character:", x[4], "\tIndex:", x.index("o"))
print("6\t\t","6th character:", x[5], "\tIndex:", x.index("n"))

# Index Out of range
#print(x[6])


# Type of Individual characters in a string.
y = "Hello @!#123\n"
print("7\t\t",y)
print("8\t\t","Y has\t", y[0], type(y[0]).__name__, "\t", y[1], type(y[1]).__name__, "\t",
      y[5],type(y[5]).__name__, "\t", y[6], type(y[6]).__name__, "\t",
      y[7], type(y[7]).__name__, "\t", y[8], type(y[8]).__name__, "\t",
      y[9], type(y[9]).__name__, "\t", y[12], type(y[12]).__name__  )



# Types of indexing:
# 1. Positive Indexing: Starts from 0 and goes to n-1 (where n is the length of the string).
a = "python"
len_a = 0
print("9\t\t","Positive Indexing:")
while len_a < len(a):
    print("\t\t\t",f"Index: {len_a}, Character: {a[len_a]}")
    len_a += 1

# 2. Negative Indexing: Starts from -1 and goes to -n (where n is the length of the string).
len_a = -1
print("10\t\t","Negative Indexing:")
while len_a >= -len(a):
    print("\t\t\t"f"Index: {len_a}, Character: {a[len_a]}")
    len_a -= 1


# Slicing of a string: string[start:end:step]
earth = "This World is Earth@290.21"
print("11\t\t",earth[0:19])
print("12\t\t",earth[:4])      # Omitting Start
print("13\t\t",earth[14:])     # Omitting End
print("14\t\t",earth[:])       # Omitting Start and End

# Negative Slicing: string[start:end:step]
print("15\t\t",earth[-1:-26]) # Wrong way. Moves forward in the string. So, it will return empty string.
print("16\t\t",earth[-26:-1]) # Correct way to reverse
print("17\t\t",earth[-21:-7])
print("18\t\t",earth[:-16])   # Omit Start
print("19\t\t",earth[-7:])    # Omit End
print("20\t\t",earth[:])      # Omit Start and End
print("21\t\t",earth[-1:-26:-1]) # Reverse a string.
print("22\t\t",len(earth))

# Step Slicing: string[start:end:step]
print("======Step Slicing======")
py = "python"
#print("23\t\t",py[0:6:0])  # ValueError: slice step cannot be zero
print("23\t\t",py[0:6:1])   # Step Slicing
print("24\t\t",py[0:6:2])   # Step Slicing
print("25\t\t",py[0:6:3])   # Step Slicing
print("26\t\t", py[5:1:-1]) # -ve Step # We don't have to take 6 as end("n") is at start("n")
# Negative Step Slicing String
print("27\t\t",py[0:6:-1])    
print("28\t\t",py[-6:-1:-1]) 
print("29\t\t",py[5:0:-1])
print("29\t\t",py[-1:-6:-1])
print("30.1\t\t",py[:6:-1])
print("30.2\t\t",py[:-1:-1])
print("31\t\t",py[0::-1])
print("32\t\t",py[-6::-1])
print("33\t\t",py[::-1])    # Reverse String
print("34\t\t",py[5::-1])   # Reverse String
print("35\t\t",py[-1::-1])  # Reverse String
# -ve and +ve index can be combined
print("36\t\t",py[0:-1:1])
print("37\t\t",py[0::1])
print("37\t\t",py[-6:6:1])
