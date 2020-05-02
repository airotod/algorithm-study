def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                print(arr)
    return arr

if __name__ == '__main__':
    test_arr1 = [6, 5, 4, 2, 3, 1, 7]
    print(f'Original array: {test_arr1}')
    print(f'Sorted array: {bubble_sort(test_arr1)}')