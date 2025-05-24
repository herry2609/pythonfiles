# pythonfiles
🐍 Setting Up Python in Visual Studio Code (VS Code)
📦 Requirements
Windows / macOS / Linux
Internet connection
#----------------------------------------------------------------------
🔽 Step 1: Download and Install VS Code
Go to the official website: https://code.visualstudio.com

Click on Download for your OS (Windows, macOS, or Linux).

Run the installer and follow the setup instructions.

During installation, make sure to check the box:
✅ "Add to PATH (recommended)"
#----------------------------------------------------------------------
🔽 Step 2: Install Python
Download Python from https://www.python.org/downloads/

Run the installer.

IMPORTANT: Check the box:
✅ "Add Python to PATH"

Click Install Now.
#----------------------------------------------------------------------
🔌 Step 3: Install Python Extension in VS Code
Open VS Code.

Go to the Extensions tab (or press Ctrl+Shift+X).

Search for Python and install the one by Microsoft.

(Optional but useful) Install Code Runner extension to run Python files easily.
#----------------------------------------------------------------------
📝 Step 4: Create and Run Python File
Open any folder in VS Code:
File → Open Folder → Select folder or create new

Click New File → name it hello.py

Write your first Python code:
python
Copy
Edit
print("Hello, world!")
#----------------------------------------------------------------------
Run the code:

Method 1: Right-click in the editor → Run Python File in Terminal

Method 2: Press Ctrl + Alt + N (if you installed Code Runner)

Method 3: Click the green ▶️ play button in the top right corner
#----------------------------------------------------------------------
🧪 Step 5: Check if Python is Working (Optional)
Open Terminal in VS Code (Ctrl+~) and type:

bash
Copy
Edit
python --version
It should show the installed Python version like:
nginx
Copy
Edit
Python 3.12.1

#----------------------------------------------------------------------

📚 Helpful Tips

Save your file before running (Ctrl+S)

Use print() to show output

Use input() to get user input

#----------------------------------------------------------------------

🛠️ Troubleshooting

❌ python not recognized: Make sure Python is added to PATH.

❌ No Python interpreter found: Press Ctrl+Shift+P → Search “Python: Select Interpreter” → Choose installed Python.

#----------------------------------------------------------------------

## 📚 Python Data Types

Python provides various built-in data types to support different kinds of data operations. These types are broadly categorized as follows:

### 🔢 Numeric Types
- `int`: Integer values (e.g., `10`, `-5`)
- `float`: Floating-point numbers (e.g., `3.14`, `-0.001`)
- `complex`: Complex numbers (e.g., `2 + 3j`)

### 🔤 Text Type
- `str`: String values, enclosed in quotes (e.g., `"hello"`, `'Python'`)

### 📦 Sequence Types
- `list`: Ordered, mutable collection (e.g., `[1, 2, 3]`)
- `tuple`: Ordered, immutable collection (e.g., `(1, 2, 3)`)
- `range`: Represents a sequence of numbers (e.g., `range(5)`)

### 📘 Mapping Type
- `dict`: Collection of key-value pairs (e.g., `{"name": "Alice", "age": 25}`)

### 🔘 Set Types
- `set`: Unordered collection of unique items (e.g., `{1, 2, 3}`)
- `frozenset`: Immutable version of a set

### ❓ Boolean Type
- `bool`: Logical values `True` or `False`

### 🈳 None Type
- `NoneType`: Represents the absence of a value (`None`)
  
-> These are the datatypes of python.

#----------------------------------------------------------------------

# Python Addition with Different Data Types (Without Functions)

This simple Python script demonstrates how to **add or concatenate** different data types using the `+` operator **without using functions** (`def`). It includes examples with:
- Integers
- Floats
- Strings
- Mixed types (integer + float)
- String with number (with type conversion)

## 🔢 Integer Addition

a = 10
b = 20
int_result = a + b
print("Integer addition result:", int_result)  # Output: 30
Explanation: Adds two integer values. The result is also an integer.

🌊 Float Addition

x = 10.5
y = 5.5
float_result = x + y
print("Float addition result:", float_result)  # Output: 16.0
Explanation: Adds two floating-point numbers. The result is a float.

🧵 String Concatenation

str1 = "Hello, "
str2 = "World!"
string_result = str1 + str2
print("String addition result:", string_result)  # Output: Hello, World!
Explanation: Using + with strings performs concatenation, not numeric addition.

🔀 Integer + Float Addition

num1 = 7
num2 = 3.5
mixed_result = num1 + num2
print("Integer + Float result:", mixed_result)  # Output: 10.5
Explanation: When adding an integer and a float, Python automatically converts the integer to a float.

⚠️ String and Number (TypeError Example)

# print("Result: " + 5)  # ❌ This will raise a TypeError
Explanation: Python does not allow adding a string and a number directly. You need to convert the number to a string first.

✅ String and Number (Correct Way)

print("Combined string and number:", "Result: " + str(5))  # Output: Result: 5
Explanation: Use str() to convert the number to a string before concatenating.

💡 Key Takeaways

+ operator works differently based on data types:
Numbers: Performs arithmetic addition.
Strings: Performs concatenation.
Python automatically handles type promotion (e.g., int + float becomes float).
Avoid mixing incompatible types (e.g., str + int) without conversion.

-> These are the Adding Numeric and Text Types.

#----------------------------------------------------------------------

✅ Adding Elements to a List.

Method	Description	Example.

| Method                | Description                                       | Example                      |
| --------------------- | ------------------------------------------------- | ---------------------------- |
| `append(item)`        | Adds an item to the **end** of the list           | `my_list.append(5)`          |
| `insert(index, item)` | Inserts an item at a specific position            | `my_list.insert(2, "hello")` |
| `extend(iterable)`    | Adds all elements from another list (or iterable) | `my_list.extend([1, 2, 3])`  |
| `+` operator          | Concatenates two lists                            | `new_list = list1 + list2`   |
| `*= n`                | Repeats the list `n` times                        | `my_list *= 3`               |


❌ Removing Elements from a List.

Method	Description	Example.

| Method         | Description                                      | Example                           |
| -------------- | ------------------------------------------------ | --------------------------------- |
| `remove(item)` | Removes the **first occurrence** of the item     | `my_list.remove("apple")`         |
| `pop()`        | Removes and returns the **last item**            | `my_list.pop()`                   |
| `pop(index)`   | Removes and returns the item at a specific index | `my_list.pop(2)`                  |
| `clear()`      | Removes **all elements** from the list           | `my_list.clear()`                 |
| `del`          | Deletes item at index or entire list             | `del my_list[1]` or `del my_list` |


🔄 Other Useful List Methods.

Method	Description	Example.

| Method         | Description                             | Example                      |
| -------------- | --------------------------------------- | ---------------------------- |
| `index(item)`  | Returns the index of the first match    | `my_list.index("banana")`    |
| `count(item)`  | Returns how many times the item appears | `my_list.count(2)`           |
| `sort()`       | Sorts the list **in-place**             | `my_list.sort()`             |
| `sorted(list)` | Returns a **new sorted list**           | `sorted(my_list)`            |
| `reverse()`    | Reverses the list **in-place**          | `my_list.reverse()`          |
| `copy()`       | Returns a shallow copy of the list      | `copy_list = my_list.copy()` |

-> These are the methods of List.

#----------------------------------------------------------------------

➕ Adding Elements to a Set.

Method	Description	Example.

| Method             | Description                                  | Example                    |
| ------------------ | -------------------------------------------- | -------------------------- |
| `add(x)`           | Adds a single item                           | `my_set.add(4)`            |
| `update(iterable)` | Adds multiple items (from list, tuple, etc.) | `my_set.update([5, 6, 7])` |

🔁 update() can accept any iterable: list, set, tuple, string, etc.

❌ Removing Elements from a Set.

Method	Description	Example.

| Method       | Description                                       | Example               |
| ------------ | ------------------------------------------------- | --------------------- |
| `remove(x)`  | Removes item `x`. Raises `KeyError` if not found. | `my_set.remove(2)`    |
| `discard(x)` | Removes item `x`. **No error** if not found.      | `my_set.discard(10)`  |
| `pop()`      | Removes and returns **any random item**           | `item = my_set.pop()` |
| `clear()`    | Empties the set                                   | `my_set.clear()`      |
| `del`        | Deletes the set entirely                          | `del my_set`          |


♻️ Set Operations.

Operation	Syntax	Description.

| Operation            | Syntax                                 | Description                      |                   
| -------------------- | -------------------------------------- | -------------------------------- |
| Union                | `a.union(b)` or \`a                    | b\`                              | 
| Intersection         | `a.intersection(b)` or `a & b`         | Common elements                  |                   
| Difference           | `a.difference(b)` or `a - b`           | Items in `a` not in `b`          |                  
| Symmetric Difference | `a.symmetric_difference(b)` or `a ^ b` | Items in `a` or `b` but not both |


✅ Set Comparison Methods.

Method	Description	Example.

| Method         | Description                                     | Example           |
| -------------- | ----------------------------------------------- | ----------------- |
| `issubset()`   | Check if all elements of one set are in another | `a.issubset(b)`   |
| `issuperset()` | Check if a set contains all elements of another | `a.issuperset(b)` |
| `isdisjoint()` | Check if two sets have no common elements       | `a.isdisjoint(b)` |


🔍 Other Useful Set Methods.

Method	Description	Example.

| Method          | Description                       | Example                   |
| --------------- | --------------------------------- | ------------------------- |
| `copy()`        | Returns a shallow copy of the set | `new_set = my_set.copy()` |
| `len()`         | Returns number of elements        | `len(my_set)`             |
| `in` / `not in` | Checks membership                 | `3 in my_set`             |


🧠 Key Points

(1) Sets are unordered, so indexing is not allowed.
(2) Automatically removes duplicate elements.
(3) Use set() constructor to create empty sets, not {}.

-> These are the methods and operation of set.

#----------------------------------------------------------------------

🧠 Important Note:

✅ Tuples are immutable → You cannot add, remove, or change their elements directly.
But you can convert to a list, modify, and convert back to a tuple.

🛠️ Useful Tuple Methods :- 

| Method     | Description                               | Example      |
| ---------- | ----------------------------------------- | ------------ |
| `count(x)` | Returns the number of times `x` appears   | `t.count(2)` |
| `index(x)` | Returns the index of the first occurrence | `t.index(3)` |

📌 Summary

| Action         | How to Do It                          |
| -------------- | ------------------------------------- |
| Add element    | `t = t + (element,)`                  |
| Remove element | Convert to list, remove, convert back |
| Count items    | `t.count(x)`                          |
| Find index     | `t.index(x)`                          |

-> These are the methods and operation of Tuple.

#----------------------------------------------------------------------

🧠 What is a Dictionary?

A dict in Python is a collection of key-value pairs. It is mutable, unordered (in older versions), and indexed by keys.

🛠️ Common Dictionary Methods :- 

| Method               | Description                                  | Example               |
| -------------------- | -------------------------------------------- | --------------------- |
| `dict.get(key)`      | Returns value of key, or `None` if not found | `d.get("name")`       |
| `dict.keys()`        | Returns a view of all keys                   | `d.keys()`            |
| `dict.values()`      | Returns a view of all values                 | `d.values()`          |
| `dict.items()`       | Returns key-value pairs                      | `d.items()`           |
| `dict.update({...})` | Adds/updates key-value pairs                 | `d.update({"a": 1})`  |
| `dict.copy()`        | Returns a shallow copy                       | `new_dict = d.copy()` |
| `dict.pop(key)`      | Removes specified key and returns its value  | `d.pop("age")`        |
| `dict.popitem()`     | Removes and returns the last key-value pair  | `d.popitem()`         |
| `dict.clear()`       | Removes all items                            | `d.clear()`           |

📌 Summary Table :- 

| Task            | Method or Syntax                       |
| --------------- | -------------------------------------- |
| Add item        | `d["key"] = value` or `update()`       |
| Remove item     | `pop()`, `popitem()`, `del`, `clear()` |
| Access value    | `d["key"]` or `get("key")`             |
| Get keys        | `d.keys()`                             |
| Get values      | `d.values()`                           |
| Get items       | `d.items()`                            |
| Copy dictionary | `d.copy()`                             |

-> These are the methods and operation of Dictionary.

#----------------------------------------------------------------------