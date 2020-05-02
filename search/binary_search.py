def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return None

def binary_search_left(arr, target):
    left = 0
    right = len(arr) - 1
    while left < right:
        mid = (left + right) // 2
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid
    return left

def binary_search_right(arr, target):
    count = 0
    left = 0
    right = len(arr) - 1
    while left < right:
        mid = (left + right) // 2
        if arr[mid] <= target:
            left = mid + 1
        else:
            right = mid
    return right

if __name__ == "__main__":
    test1_arr, test1_n = [1, 11, 111, 1111, 11111], 11
    test2_arr, test2_n = [1, 11, 111, 1111, 11111], 22
    print(f'arr: {test1_arr}, n: {test1_n}, return: {binary_search(test1_arr, test1_n)}')  # return 1
    print(f'arr: {test2_arr}, n: {test2_n}, return: {binary_search(test2_arr, test2_n)}')  # return None

    test3_arr, test3_n = [1, 1, 1, 1, 1], 1
    print(f'arr: {test3_arr}, n: {test3_n}, return: {binary_search(test3_arr, test3_n)}')        # return 2
    print(f'arr: {test3_arr}, n: {test3_n}, return: {binary_search_left(test3_arr, test3_n)}')   # return 0
    print(f'arr: {test3_arr}, n: {test3_n}, return: {binary_search_right(test3_arr, test3_n)}')  # return 4