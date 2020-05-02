def climbing_stairs(arr):
    n = arr[0]
    if n == 1:
        return arr[1]

    stairs = [0] * (n+1)
    for i in range(n):
        stairs[i+1] = arr[i+1]

    mem = [[0]*2 for _ in range(n+1)]
    mem[1][0] = stairs[1]

    for step in range(2, n+1):
        mem[step][1] = mem[step-1][0] + stairs[step]
        mem[step][0] = max(mem[step-2][0], mem[step-2][1]) + stairs[step]

    return(max(mem[-1]))

if __name__ == "__main__":
    test_arr1 = [6, 10, 20, 15, 25, 10, 20]  # 75
    print(f'input: {test_arr1}')
    print(f'max score: {climbing_stairs(test_arr1)}')