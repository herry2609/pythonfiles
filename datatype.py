# Examples of Datatypes.

### 🔢 Numeric Types.

#(1) Integer

a = 12
print(a)  # the print() function is used to display output on the screen (console).
print(type(a)) #type(obj) → returns the type of the object.
# output:- ( <class 'int'> )
#ANS :-  integer 

#(2) Float

x = 3.14 #The value of pi.
print(x)  # output :-  3.14
print(type(x))   # output:- ( <class 'float'> )

#(3) Complex

b = 3 + 2j # A complex number is a number that has two parts:(A real part) and (An imaginary part).
print(b)   # output :- (3+2j)
#here 3 is the real part, 2 is the imaginary part and j is the imaginary unit in Python (equivalent to i in mathematics).
print(type(b))   # output:- ( <class 'complex'> )

#----------------------------------------------------------------------

### 🔤 Text Type.

# String
y = "hello world" 'hello python'    # We use the (" ") double or (' ') single inverted comma.
print(y) # output :- hello worldhello python
print(type(y))   # output:- ( <class 'str'> )

#----------------------------------------------------------------------

### 📦 Sequence Types.

#(1) List
# denoted by ( '[ ]' ) square bracket.
 
c = [1,2,"hello",3.14]
print(c)  # output :- [1,2,"hello",3.14]
print(type(c))   # output:- ( <class 'list'> )

#(2) Tuple
# denoted by ( '( )' ) square bracket.

z = (10,3.14,"hello python!!")
print(z) # output :- (10,3.14,"hello python!!")
print(type(z))  # output:- ( <class 'tuple'> )

#(3) Range

r = range(5)
print(r)  # output :- (0,5)           
print(type(r))  # output:- ( <class 'range'> )

#----------------------------------------------------------------------

### 📘 Mapping Type.

# Dictionary :- Collection of key-value pairs.
#denoted by ( '{key:value}' ) curly bracket.

dict1 = {"Name":"Herry","City":"Surat","Lang":"Gujarati"}
print(dict1)    # output :- {"Name":"Herry","City":"Surat","Lang":"Gujarati"}
print(type(dict1))  # output:- ( <class 'dict'> )

#----------------------------------------------------------------------

### 🔘 Set Types.

#(1) Set 
#denoted ( '{ }' )

s1 = {1,3.14,"python","world"}
print(s1) # Output :- {1,3.14,"python","world"}
print(type(s1))     # output:- ( <class 'set'> )

#(2) Frozenset

# Creating a normal set
s = {1, 2, 3}

# Creating a frozenset from the set
fs = frozenset(s)

print(fs)           # Output: frozenset({1, 2, 3})
print(type(fs))    # output:- ( <class 'frozenset'> ) 

#----------------------------------------------------------------------

### ❓ Boolean Type

a = True
b = False

print(a)    # Output:- True
print(b)    # Output:- False

print(type(a))   # Output: (<class 'bool'>)
print(type(b))   # Output: (<class 'bool'>)

#----------------------------------------------------------------------

### 🈳 None Type

x = None

print(x)             # Output: None
print(type(x))       # Output: (<class 'NoneType'>)

#----------------------------------------------------------------------