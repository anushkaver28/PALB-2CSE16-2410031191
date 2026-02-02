def find_union(arr1, arr2):
    return sorted(list(set(arr1) | set(arr2)))


a = [4, 9, 1, 5, 2]
b = [8, 7, 6, 3, 9]

print("Array a:", a)
print("Array b:", b)

union_result = find_union(a, b)


print("\nExplanation:")
print("Unique elements in a:", set(a))
print("Unique elements in b:", set(b))
print("Union (all unique elements combined):", union_result)