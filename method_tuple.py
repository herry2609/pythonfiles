# Original tuple
t = (1, 2, 3)

# Adding an element (e.g., 4) using concatenation
t = t + (4,)  # Must use a trailing comma to make it a tuple

print("Tuple after adding an element:", t)

#----------------------------------------------------------------------

# Original tuple
t = (1, 2, 3, 4)

# Convert tuple to list for modification
temp_list = list(t)

# Remove the element (e.g., 3)
temp_list.remove(3)

# Convert back to tuple
t = tuple(temp_list)

print("Tuple after removing an element:", t)

#----------------------------------------------------------------------

# Tuple creation
my_tuple = (10, 20, 30, 40, 30)

# ------------------------
# 1. Tuple is immutable, so to add or remove:
# Convert to list -> modify -> convert back to tuple
# ------------------------

# "Add" an element
my_tuple = my_tuple + (50,)  # Adding 50 to the tuple

# "Remove" an element by converting to list
temp_list = list(my_tuple)
temp_list.remove(20)         # Removing 20
my_tuple = tuple(temp_list)  # Converting back to tuple

# ------------------------
# 2. Tuple methods
# ------------------------

# Count occurrences of 30
count_30 = my_tuple.count(30)

# Find index of first 30
index_30 = my_tuple.index(30)

# ------------------------
# 3. Output
# ------------------------
print("Final tuple:", my_tuple)
print("Count of 30:", count_30)
print("Index of 30:", index_30)