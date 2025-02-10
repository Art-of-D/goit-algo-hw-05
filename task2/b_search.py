def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    iterations = 0
    upper_bound = None

    while low <= high:
        iterations += 1
        mid = (low + high) // 2

        if arr[mid] == target:
            return iterations, arr[mid] 

        if arr[mid] < target:
            low = mid + 1
        else:
            upper_bound = arr[mid] 
            high = mid - 1

    return iterations, upper_bound

arr = [0.5, 1.2, 3.2, 3.9, 4.1, 5.3, 7.8, 7.9, 8.0, 8.1, 8.6, 9.9]
target = 4.0
print(binary_search(arr, target))