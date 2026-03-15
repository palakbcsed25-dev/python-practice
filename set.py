set1 = {1, 2, 4, 3}
set2 = {3, 4, 5}
union_set = set1.union(set2)
print(union_set)  # Output: {1, 2, 3, 4, 5}
union_set = set1 | set2
print(union_set)  # Output: {1, 2, 3, 4, 5}


# Intersection
# Returns a new set containing only elements that are in both sets.

set1 = {1, 2, 4,3}
set2 = {3, 4, 5}
intersection_set = set1.intersection(set2)
print(intersection_set)  # Output: {3}

# Or using the `&` operator:

intersection_set = set1 & set2
print(intersection_set)  # Output: {3}


# Difference
# Returns a new set containing elements that are in the first set but not in the second.

set1 = {1, 4, 3}
set2 = {3, 4, 5}
difference_set = set1.difference(set2)
print(difference_set)  # Output: {1, 2}