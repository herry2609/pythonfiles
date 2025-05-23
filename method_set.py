# These are the operation of the set.

a = {1, 2, 3}
b = {3, 4, 5}

print(a | b)   # Union: {1, 2, 3, 4, 5}
print(a & b)   # Intersection: {3}
print(a - b)   # Difference: {1, 2}
print(a ^ b)   # Symmetric Difference: {1, 2, 4, 5}

# These are the methods of a set.

s = {1, 2, 3}

# Add elements
s.add(4)
s.update([5, 6])

# Remove elements
s.remove(1)
s.discard(10)  # No error if 10 is not in set

# Set operations
a = {1, 2, 3}
b = {3, 4, 5}

print(a.union(b))        # {1, 2, 3, 4, 5}
print(a.intersection(b)) # {3}
print(a.difference(b))   # {1, 2}
print(a.symmetric_difference(b))  # {1, 2, 4, 5}

# Example of Set Comparison Methods in Python

# Set A contains two elements
A = {1, 2}

# Set B contains more elements including all of A's elements
B = {1, 2, 3, 4}

# Set C has elements that are completely different from A
C = {5, 6}

# ------------------------------------
# issubset(): Checks if A is a subset of B
# Means: Are all elements of A present in B?
print("A is subset of B:", A.issubset(B))  # True
print("B is subset of A:", B.issubset(A))  # False

# ------------------------------------
# issuperset(): Checks if A is a superset of B
# Means: Does A contain all elements of B?
print("A is superset of B:", A.issuperset(B))  # False
print("B is superset of A:", B.issuperset(A))  # True

# ------------------------------------
# isdisjoint(): Checks if A and C have no common elements
# Returns True if they have nothing in common
print("A and C are disjoint:", A.isdisjoint(C))  # True
print("A and B are disjoint:", A.isdisjoint(B))  # False (they share 1 and 2)

# ------------------------------------

# Creating a normal set
normal_set = {1, 2, 3, 4}
print("Normal set:", normal_set)

# Creating a frozenset from a list
frozen = frozenset([3, 4, 5, 6])
print("Frozenset:", frozen)

# -----------------------------
# ❌ Modifying frozen set will raise an error
# frozen.add(7)       # ❌ AttributeError
# frozen.remove(3)    # ❌ AttributeError

# ✅ You can still perform these operations:

# Union: elements from both sets (no duplicates)
print("Union:", normal_set.union(frozen))  # {1, 2, 3, 4, 5, 6}

# Intersection: common elements
print("Intersection:", normal_set.intersection(frozen))  # {3, 4}

# Difference: elements in normal_set but not in frozen
print("Difference:", normal_set.difference(frozen))  # {1, 2}

# Symmetric difference: elements in either set but not both
print("Symmetric Difference:", normal_set.symmetric_difference(frozen))  # {1, 2, 5, 6}

# Membership test
print("Is 3 in frozen set?", 3 in frozen)  # True

# Length of frozenset
print("Length of frozenset:", len(frozen))  # 4

# Iterate through frozenset
print("Elements in frozenset:")
for item in frozen:
    print(item)