# Create an empty dictionary
student = {}

# Add a key-value pair
student["name"] = "Alice"

# Add multiple key-value pairs at once using update()
student.update({"age": 20, "grade": "A"})

print("After adding:", student)

#----------------------------------------------------------------------

# Remove a specific key using pop()
student.pop("age")  # Removes 'age'

# Remove the last inserted item using popitem()
student.popitem()  # Removes 'grade'

# Remove a specific key using del
del student["name"]  # Deletes the key 'name'

# Clear all items
student.clear()  # Now student = {}

print("After removing:", student)

#----------------------------------------------------------------------

# 1. Creating a dictionary
student = {
    "name": "Alice",
    "age": 20,
    "grade": "A"
}

# 2. Adding elements
student["email"] = "alice@example.com"         # Add new key-value pair
student.update({"city": "New York"})           # Add another using update()

# 3. Accessing values
print("Student Name:", student["name"])        # Access using key
print("Student Email:", student.get("email"))  # Access using get()

# 4. Getting keys, values, and items
print("Keys:", student.keys())
print("Values:", student.values())
print("Items:", student.items())

# 5. Copying the dictionary
backup = student.copy()

# 6. Removing elements
student.pop("grade")       # Removes grade
student.popitem()          # Removes last inserted (city)
del student["email"]       # Removes email

# 7. Final dictionary after removals
print("After removals:", student)

# 8. Clear all items
student.clear()
print("After clearing:", student)

# 9. The backup is still intact
print("Backup copy:", backup)