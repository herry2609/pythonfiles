# Examples of Datatypes.

### 🔢 Numeric Types.

#(1) Integer

a = 12
print(a)  # the print() function is used to display output on the screen (console).
print(type(a)) #type(obj) → returns the type of the object.
#ANS :-  integer in terminal ( <class 'int'> )

#(2) Float

x = 3.14 #The value of pi.
print(x)  # output :-  3.14
print(type(x))   #ANS :-  float in terminal ( <class 'float'> )

#(3) Complex

b = 3 + 2j # A complex number is a number that has two parts:(A real part) and (An imaginary part).
print(b)   # output :- (3+2j)
#here 3 is the real part, 2 is the imaginary part and j is the imaginary unit in Python (equivalent to i in mathematics).
print(type(b))   #ANS :- complex in terminal ( <class 'complex'> )

### 🔤 Text Type.

# String
y = "hello world" 'hello python'    # We use the (" ") double or (' ') single inverted comma.
print(y) # output :- hello worldhello python
print(type(y))   #ANS :-  string in terminal ( <class 'str'> )

### 📦 Sequence Types.

#(1) List
# denoted by ( '[ ]' ) square bracket.
 
c = [1,2,"hello",3.14]
print(c)  # output :- [1,2,"hello",3.14]
print(type(c))   #ANS :-  list in terminal ( <class 'list'> )

#(2) Tuple
# denoted by ( '( )' ) square bracket.

z = (10,3.14,"hello python!!")
print(z) # output :- (10,3.14,"hello python!!")
print(type(z))  #ANS :-  tuple in terminal ( <class 'tuple'> )

#(3) Range

r = range(5)
print(r)  # output :- (0,5)           
print(type(r))  #ANS :-  range in terminal ( <class 'range'> )

