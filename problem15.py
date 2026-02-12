#MERGE TWO SORTED ARRAYS WITHOUT EXTRA SPACE

a = [1, 5, 9, 10, 15, 20]
b = [2, 3, 8, 13]

n = len(a)
m = len(b)

i = n - 1
j = 0

while i >= 0 and j < m:
    if a[i] > b[j]:
        a[i], b[j] = b[j], a[i]
    i -= 1
    j += 1

a.sort()
b.sort()

print("Array a:", a)
print("Array b:", b)