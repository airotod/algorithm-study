def heapify(arr, idx, size):
    max_idx = idx
    left_idx = 2 * idx + 1
    right_idx = 2 * idx + 2
    if (left_idx < size) and (arr[left_idx] > arr[max_idx]):
        max_idx = left_idx
    if (right_idx < size) and (arr[right_idx] > arr[max_idx]):
        max_idx = right_idx
    if max_idx != idx:
        arr[max_idx], arr[idx] = arr[idx], arr[max_idx]
        heapify(arr, max_idx, size)

def heap_sort(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, i, n)
    for i in range(n-1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, 0, i)
    return arr

if __name__ == '__main__':
    test_arr1 = [6, 5, 4, 2, 3, 1, 7]
    print(f'Original array: {test_arr1}')
    print(f'Sorted array: {heap_sort(test_arr1)}')