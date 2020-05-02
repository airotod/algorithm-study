def merge_sort(arr):
    n = len(arr)
    if n > 1:
        mid_idx = n // 2

        left_arr = arr[:mid_idx]
        right_arr = arr[mid_idx:]

        left_arr = merge_sort(left_arr)
        right_arr = merge_sort(right_arr)

        return merge(left_arr, right_arr)
    return arr

def merge(arr1, arr2):
    result = []

    while (len(arr1) > 0) or (len(arr2) > 0):
        if (len(arr1) > 0) and (len(arr2) > 0):
            if arr1[0] <= arr2[0]:
                result.append(arr1.pop(0))
            else:
                result.append(arr2.pop(0))
        elif len(arr1) > 0:
            result.append(arr1.pop(0))
        elif len(arr2) > 0:
            result.append(arr2.pop(0))

    return result

if __name__ == '__main__':
    test_arr1 = [6, 5, 4, 2, 3, 1, 7]
    print(f'Original array: {test_arr1}')
    print(f'Sorted array: {merge_sort(test_arr1)}')