def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

arr = [10, 23, 45, 70, 11, 15]
target = 70
print(f"Element found at index: {linear_search(arr, target)}")
