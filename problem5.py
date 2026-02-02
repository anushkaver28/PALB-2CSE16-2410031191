def find_largest(arr):
    largest = arr[0]
 
    for i in range(1, len(arr)):
        if arr[i] > largest:
            largest = arr[i]
            
   
    return largest


arr = [22, 48, 2, 8, 34, 59, 66]
print("Array:", arr)

result = find_largest(arr)

print("Output:", result)
print("\nExplanation: The largest element in the array is = ", result)