def move_zeros_to_end(arr):
    write_index = 0
    for read_index in range(len(arr)):
        if arr[read_index] != 0:
            arr[write_index] = arr[read_index]
            write_index += 1

    while write_index < len(arr):
        arr[write_index] = 0
        write_index += 1


n = int(input())
arr = list(map(int, input().split()))

move_zeros_to_end(arr)
print(' '.join(map(str, arr)))
