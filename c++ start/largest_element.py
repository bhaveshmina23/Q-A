arr = [1,2,5,9,6,3]
n=6

largest = arr[0]
for i in range(n):
    if arr[i] > largest:
        largest = arr[i]
print("first answer", largest)

#another approach
arr.sort()
print("another approach", arr[-1])