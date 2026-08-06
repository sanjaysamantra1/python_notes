set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# 1. union() → All items from both sets
print(set1.union(set2))
# {1, 2, 3, 4, 5, 6}


# 2. intersection() → ONLY common/duplicate items
print(set1.intersection(set2))
# {3, 4}


# 3. difference() → Items in set1 but NOT in set2
print(set1.difference(set2))
# {1, 2}


# 4. symmetric_difference() → All items EXCEPT common items
print(set1.symmetric_difference(set2))
# {1, 2, 5, 6}