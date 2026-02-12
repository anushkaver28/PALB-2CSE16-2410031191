#TWO SUM PROBLEM

nums = [12, 7, 10, 11]
target = 17

for i in range(len(nums)):


    for j in range(i + 1, len(nums)):
        if nums[i] + nums[j] == target:


            print("Indices:", [i, j])
            break