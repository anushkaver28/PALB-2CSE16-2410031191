def rotate_by_one(arr):
    n = len(arr)

    if n <= 1:
        return arr

    last = arr[-1]

    for i in range(n - 1, 0, -1):
        arr[i] = arr[i - 1]

    arr[0] = last
    return arr


arr = [3, 4, 5, 6, 7]


rotated_arr = rotate_by_one(arr)


print(rotated_arr)
