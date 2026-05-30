def find_even_index(arr):
    for i in range(len(arr)):
        left = arr[:i]
        right = arr[i+1:]

        if sum(left) == sum(right):
            return i

    return -1
