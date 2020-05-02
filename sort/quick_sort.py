def quick_sort(arr):
    n = len(arr)
    if n > 1:
        pivot = arr[0]
        large_arr = [x for x in arr[1:] if x > pivot]
        small_arr = [x for x in arr[1:] if x <= pivot]
        return quick_sort(small_arr) + [pivot] + quick_sort(large_arr)
    return arr

if __name__ == '__main__':
    test_arr1 = [6, 5, 4, 2, 3, 1, 7]
    print(f'Original array: {test_arr1}')
    print(f'Sorted array: {quick_sort(test_arr1)}')