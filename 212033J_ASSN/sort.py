# Name: Xu Yong Lin
# Admin no: 212033J
# Tutorial group: IT2153-01

# bubble sort record by customer name
def bubble_sort(elements):
    # best case: omega(n) worse case: O(n^2)
    n = len(elements)
    for i in range(n):
        for j in range(0, n - i - 1):
            if elements[j].customername > elements[j + 1].customername:
                elements[j], elements[j + 1] = elements[j + 1], elements[j]
    return elements


# selection sort record by package name
def selection_sort(L):
    # best case: omega(n^2) worse case: O(n^2)
    for i in range(len(L) - 1):
        min_index = i
        for j in range(i + 1, len(L)):
            if L[j].packagename < L[min_index].packagename:
                min_index = j
        L[i], L[min_index] = L[min_index], L[i]
    return L


# insertion sort record by package cost
def insertion_sort(list):
    # best case: omega(n) worse case: O(n^2)
    for i in range(1, len(list)):
        key = list[i]
        j = i - 1
        while j >= 0 and key.packagecost < list[j].packagecost:
            list[j + 1] = list[j]
            j -= 1
        list[j + 1] = key
    return list


# radix sort record by total cost
def countingSort(array, place):
    # best case/worse case: O(n+k)
    # counting sort to sort record in the basis of significant places
    size = len(array)
    output = [0] * size
    count = [0] * 10
    # Calculate count of elements
    for i in range(0, size):
        index = array[i].totalcost // place
        count[(index % 10)] += 1
    # Calculate cumulative count
    for i in range(1, 10):
        count[i] += count[i - 1]
    # for i in range(8, 0 - 1, -1):     # reverse
    #     count[i] += count[i + 1]      # reverse
    # Place the elements in sorted order
    i = size - 1
    while i >= 0:
        index = array[i].totalcost // place
        output[count[index % 10] - 1] = array[i]
        count[index % 10] -= 1
        i -= 1

    for i in range(0, size):
        array[i] = output[i]


def radixSort(array):
    # best & worse case: O(nk)
    # if all numbers to be sorted are distinct, it will be O(n log n)
    max_element = max(array, key=lambda item: item.totalcost)

    place = 1
    while max_element.totalcost // place > 0:
        countingSort(array, place)  # calling countingSort to sort elem based on place val
        place *= 10
    return array


# radix sort record by package cost
def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    # See if left child of root exists and is greater than root
    if left < n and arr[largest].packagecost < arr[left].packagecost:
        largest = left

    # See if right child of root exists and is greater than root
    if right < n and arr[largest].packagecost < arr[right].packagecost:
        largest = right

    # Change root, if needed
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heapSort(arr):
    # best/worse case: O(n log n)
    n = len(arr)
    # Build a maxheap.
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    # One by one extract elements
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # swap
        heapify(arr, i, 0)
