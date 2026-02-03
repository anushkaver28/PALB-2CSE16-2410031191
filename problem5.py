def find_largest(arr):
    largest = arr[0]
 
    for i in range(1, len(arr)):
        if arr[i] > largest:
            largest = arr[i]
            
   
    return largest


arr = [12, 58, 22, 18, 4, 9, 62]
print("Array:", arr)

result = find_largest(arr)

print("Output:", result)
print("\nExplanation: The largest element in the array is = ", result)