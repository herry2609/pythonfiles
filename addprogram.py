# Add program

# Adding two integers

a = 10         # First integer
b = 20         # Second integer
int_result = a + b  # Adding integers
print("Integer addition result:", int_result)  # Output: 30

# Adding two floats

x = 10.5       # First float
y = 5.5        # Second float
float_result = x + y  # Adding floats
print("Float addition result:", float_result)  # Output: 16.0

# Adding (concatenating) two strings

str1 = "Hello, "      # First string
str2 = "World!"       # Second string
string_result = str1 + str2  # Concatenating strings
print("String addition result:", string_result)  # Output: Hello, World!

# Adding an integer and a float (Python automatically promotes to float)

num1 = 7      # Integer
num2 = 3.5    # Float
mixed_result = num1 + num2
print("Integer + Float result:", mixed_result)  # Output: 10.5

# Note: Adding a string and a number directly will cause an error
# Uncommenting the below line will give an error
# print("Result: " + 5)  # TypeError

# If you want to combine string and number, convert the number to string

print("Combined string and number:", "Result: " + str(5))  # Output: Result: 5