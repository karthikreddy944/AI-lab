def bubble_sort(arr):
    n = len(arr)

    for i in range(n - 1):
        for j in range(n - i - 1):

            if arr[j] > arr[j + 1]:
                
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


arr = [3,2,56,34,12]

bubble_sort(arr)

print("Sorted array:", arr)
