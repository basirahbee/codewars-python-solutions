def find_it(arr):
    for num in arr:
        if arr.count(num) % 2 != 0:
            return num
