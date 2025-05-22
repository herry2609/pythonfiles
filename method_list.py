#This is a example of list methods.

my_list = [3, 1, 4]

# Add elements
my_list.append(5)
my_list.insert(1, 2)
my_list.extend([6, 7])

# Remove elements
my_list.remove(4)
popped_item = my_list.pop()
my_list.clear()

# Other operations
my_list = [5, 2, 8, 2]
count_twos = my_list.count(2)
index_of_five = my_list.index(5)
my_list.sort()
my_list.reverse()
copied_list = my_list.copy()

print("Final list:", my_list)