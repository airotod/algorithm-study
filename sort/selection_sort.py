def selection_sort(arr):
    n = len(arr)
    for i in range(n-1):
        min_idx = i
        for j in range(i+1, n):
            if arr[min_idx] > arr[j]:
                min_idx = j
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            print(arr)
    return arr

if __name__ == '__main__':
    test_arr1 = [6, 5, 4, 2, 3, 1, 7]
    print(f'Original array: {test_arr1}')
    print(f'Sorted array: {selection_sort(test_arr1)}')