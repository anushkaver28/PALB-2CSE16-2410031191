#PRINT ALL COMMON ELEMENTS IN THREE SORTED ARRAYS
def common_elements(arr1, arr2, arr3):
    i = j = k = 0
    n1, n2, n3 = len(arr1), len(arr2), len(arr3)
    result = []

    while i < n1 and j < n2 and k < n3:
        if arr1[i] == arr2[j] == arr3[k]:
            result.append(arr1[i])
            i += 1
            j += 1
            k += 1
        elif arr1[i] < arr2[j]:
            i += 1
        elif arr2[j] < arr3[k]:
            j += 1
        else:
            k += 1

    return result if result else [-1]


# Example
print(common_elements([1,5,10,20,40,80],
                      [6,7,20,80,100],
                      [3,4,15,20,30,70,80]))
