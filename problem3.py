def kth_smallest(arr, k):
   
    return sorted(arr)[k - 1]

arr = [17, 3, 2, 8, 5, 1]
k = 3

print("Input array:", arr)
print("k =", k)

result = kth_smallest(arr, k)

print("Output:", result)
print("\nExplanation:")
print("After sorting:", end=" ")


sorted_arr = []
for i in range(len(arr)):
    sorted_arr.append(arr[i])

for i in range(len(sorted_arr)):
    for j in range(0, len(sorted_arr) - i - 1):
        if sorted_arr[j] > sorted_arr[j + 1]:
            temp = sorted_arr[j]
            sorted_arr[j] = sorted_arr[j + 1]
            sorted_arr[j + 1] = temp

print(sorted_arr)
print("The", k, " smallest element is", result)