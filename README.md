# pythonfiles
#----------------------------------------------------------------------
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
  
#-> These are the datatypes of python.