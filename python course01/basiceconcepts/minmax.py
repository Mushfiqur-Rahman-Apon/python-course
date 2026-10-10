n = int(input())
arr = list(map(int, input().split()))

min_value = min(arr)
max_value = max(arr)

min_index = arr.index(min_value)
max_index = arr.index(max_value)

arr[min_index], arr[max_index] = arr[max_index], arr[min_index]

print(*arr)
                                         