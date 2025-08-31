# Selection Sort (Descending Order)

arr = [64, 25, 12, 22, 11]
n = len(arr)

for i in range(n - 1):
    max_index = i   # assume first element is largest
    for j in range(i + 1, n):
        if arr[j] > arr[max_index]:  # only change < to >
            max_index = j
    # Swap
    arr[i], arr[max_index] = arr[max_index], arr[i]

print("Sorted array in descending order:", arr)
