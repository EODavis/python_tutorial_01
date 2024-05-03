def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)


def quicksort_verbose(arr):
    print(f'Calling quicksort on {arr}')
    if len(arr) <= 1:
        print(f'return back {arr}')
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    print(f'left: {left}; ', end="")
    middle = [x for x in arr if x == pivot]
    print(f'middle: {middle}; ', end="")
    right = [x for x in arr if x > pivot]
    print(f'right: {right}')
    to_return = quicksort(left) + middle + quicksort(right)
    print(f'return finally: {to_return}')
    return to_return


data = [3, 1, 4, 2, 5, 7, 0]
data_1 = [5, 3, 8, 6, 3, 2, 8, 7, 4]

print(quicksort(data))
print()
print(quicksort_verbose(data))
print()
print()
print(quicksort(data_1))
print()
print(quicksort_verbose(data_1))
