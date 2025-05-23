# ✅ BOOLEAN (bool) Examples

# Boolean values are True or False
is_raining = True
is_sunny = False

print("Is it raining?", is_raining)   # True
print("Is it sunny?", is_sunny)       # False

# Boolean expressions using comparisons
a = 10
b = 5

print("a > b:", a > b)         # True
print("a == b:", a == b)       # False
print("a != b:", a != b)       # True

# Boolean logic with and/or/not
print("a > 5 and b < 10:", a > 5 and b < 10)   # True
print("not is_sunny:", not is_sunny)          # True

# ------------------------------------

# ✅ NONE TYPE (NoneType) Example

# None is a special constant in Python that means "no value" or "empty"
result = None

print("Result is:", result)         # None

# Checking if a variable is None
if result is None:
    print("No result available")    # This will be printed

# Function returning None by default
def say_hello():
    print("Hello!")

output = say_hello()  # Prints "Hello!" but returns None
print("Function output:", output)  # None

# Using None as a placeholder for future assignment
data = None
# Later in program...
data = "Some value"
print("Updated data:", data)  # "Some value"