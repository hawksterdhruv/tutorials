import random

N = 200000
unsorted_list = [random.randint(0, N * 10) for i in range(N)]
# unsorted_list = [i for i in range(10)]

# print(unsorted_list)

n = len(unsorted_list)
count = 0


def partition(arr, start, end):
    pi = start

    for i in range(start, end - 1):
        if arr[i] < arr[end - 1]:
            arr[i], arr[pi] = arr[pi], arr[i]
            pi += 1
    return pi


def quicksort(arr, start, end):
    # global count
    # count += 1
    # if count > 10:
    #     return
    # print(arr[start:end])
    if start >= end:
        return

    pi = partition(arr, start, end)
    # print(arr, pi)
    arr[end - 1], arr[pi] = arr[pi], arr[end - 1]
    quicksort(arr, start, pi)
    quicksort(arr, pi + 1, end)


quicksort(unsorted_list, 0, n)
# print(unsorted_list)

for i in range(N - 1):
    if unsorted_list[i] > unsorted_list[i + 1]:
        print(False)
        break
else:
    print(True)
