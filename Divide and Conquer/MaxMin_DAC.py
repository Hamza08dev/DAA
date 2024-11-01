def MaxMin(arr, i, j):
    # Base case: if there's only one element
    if i == j:
        return arr[i], arr[i]  # return (max, min)

    # Base case: if there are two elements
    elif i == j - 1:
        if arr[i] > arr[j]:
            return arr[i], arr[j]  # (max, min)
        else:
            return arr[j], arr[i]  # (max, min)

    # Recursive case
    else:
        mid = (i + j) // 2
        left_max, left_min = MaxMin(arr, i, mid)
        right_max, right_min = MaxMin(arr, mid + 1, j)

        # Combine results
        return max(left_max, right_max), min(left_min, right_min)

# Example usage
arr = [12, 3, 5, 7, 19, 2, 18]
max_value, min_value = MaxMin(arr, 0, len(arr) - 1)
print("Max:", max_value)
print("Min:", min_value)
