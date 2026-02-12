#MINIMUM NUMBER OF JUMPS TO REACH END

arr = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]

n = len(arr)

if n == 1:
    print(0)
elif arr[0] == 0:
    print(-1)
else:
    jumps = 1
    maxReach = arr[0]
    step = arr[0]

    for i in range(1, n):
        if i == n - 1:
            print(jumps)
            break

        maxReach = max(maxReach, i + arr[i])
        step -= 1

        if step == 0:
            jumps += 1
            if i >= maxReach:
                print(-1)
                break
            step = maxReach - i
