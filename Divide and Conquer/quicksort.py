def partition(arr, l, r):
    x = arr[l]
    i = l
    for j in range(l + 1, r + 1):  # Iterate up to r
        if arr[j] <= x:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i], arr[l] = arr[l], arr[i]
    return i


def quicksort(arr, l, r):
    if l < r:
        m = partition(arr, l, r)
        quicksort(arr, l, m - 1)
        quicksort(arr, m + 1, r)


arr = [10, 7, 8, 9, 1, 5]
n = len(arr)

quicksort(arr, 0, n - 1)

for val in arr:
    print(val, end=" ")
