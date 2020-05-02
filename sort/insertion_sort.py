def insertion_sort(arr):
    n = len(arr)
    i = 1
    for i in range(i, n):
        key = arr[i]
        j = i - 1
        while (j >= 0) and (arr[j] > key):
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
        print(arr)
    return arr

if __name__ == '__main__':
    test_arr1 = [6, 5, 4, 2, 3, 1, 7]
    print(f'Original array: {test_arr1}')
    print(f'Sorted array: {insertion_sort(test_arr1)}')