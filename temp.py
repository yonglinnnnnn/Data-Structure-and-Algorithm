# numbers = [1,2,3,4,5,6,7,8]
# print(numbers[-4:])
#
# x = 'one'
# print(type(x))
#
# print('Covid-19: Stay home, Singapre' [100:200])
#
# for r in range(5):
#     for c in range(r+1):
#         print('#', end='') # print with no newline
#     print()
#
# print()
#
# for r in range(5):
#     for c in range(r):
#         print(' ', end='') # print with no newline
#     print('#')
#
# print()
#
# for r in range(5,0,-1):
#     for c in range(r-1):
#         print(' ', end='') # print with no newline
#     print('#')
#
# values = [2] * 5
# print(values)

# for r in range(5,0,-1):
#     for c in range(r):
#           print('#', end='') #Print with no newline
#     print()

# for r in range(5, 0, -1):
#     for c in range(r - 1):
#         print(' ', end='')  # Print with no newline
#     print('#')
#
# for r in range(5):
#
#     for c in range(r + 1):
#         print('#', end='')  # Print with no newline
#
#     print()
#
# for r in range(5):
#
#     for c in range(r):
#         print(' ', end='')  # Print with no newline
#
#     print('#')


# done by Xu Yong Lin


def sequentialSearch(theValues, target):
    n = len(theValues)
    for i in range(n):
        if theValues[i] == target:
            return True
        elif theValues[i] > target:
            return False
    return False  # If not found, return False


# Done by Xu Yong Lin (212033J)
def binarySearch(theValues, target):
    low = 0
    high = len(theValues) - 1
    while low <= high:
        mid = (high + low) // 2
        if theValues[mid] == target:
            while theValues[mid - 1] == target:
                mid -= 1
            return mid
        elif theValues[mid] < target:
            low = mid - 1
        else:
            low = mid + 1
    return "not found"


def countingSort(arr, exp1):
    n = len(arr)

    # The output array elements that will have sorted arr
    output = [0] * (n)

    # initialize count array as 0
    count = [0] * (10)

    # Store count of occurrences in count[]
    for i in range(0, n):
        index = (arr[i] / exp1)
        count[int((index) % 10)] += 1

    # Change count[i] so that count[i] now contains actual
    # position of this digit in output array
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Build the output array
    i = n - 1
    while i >= 0:
        index = (arr[i] / exp1)
        output[count[int((index) % 10)] - 1] = arr[i]
        count[int((index) % 10)] -= 1
        i -= 1
    # print(output)

    # Copying the output array to arr[],
    # so that arr now contains sorted numbers
    i = 0
    for i in range(len(arr)):
        arr[i] = output[i]
        # i -= 1


def Radix_Sort(array):
    largest_number = max(array)
    place_value = 1
    while largest_number / place_value > 0:
        countingSort(array, place_value)
        place_value *= 10


array = [112, 113, 70, 23, 55, 120]
Radix_Sort(array)
for i in range(len(array)):
    print(array[i])
