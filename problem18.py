#CHECK IF B IS SUBSET OF A
def is_subset(a, b):
    return set(b).issubset(set(a))


# Example
print(is_subset([11,7,1,13,21,3,7,3], [11,3,7,1]))
