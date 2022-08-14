# Name: Xu Yong Lin
# Admin no: 212033J
# Tutorial group: IT2153-01

def selectionSort(theSeq, sortOrder):
    n = len(theSeq)
    # for ascending
    for i in range(n - 1):
        # Assume the ith element is the smallest.
        Ndx = i
        # Determine if any other element contains a smaller value.
        for j in range(i + 1, n):
            if sortOrder.upper() == "A":
                if theSeq[j] < theSeq[Ndx]:
                    Ndx = j
            elif sortOrder.upper() == "D":
                if theSeq[j] > theSeq[Ndx]:
                    Ndx = j
        # Swap the ith value and smallNdx value only if the
        # smallest value is not already in its proper position.
        if Ndx != i:
            tmp = theSeq[i]
            theSeq[i] = theSeq[Ndx]
            theSeq[Ndx] = tmp

    # sorting in descending order.


# Test codes
print('sorting in ascending order')
list_of_numbers = [10, 51, 2, 18, 4, 31, 13, 5, 23, 64, 29]
print('Input List:', list_of_numbers)

# ascending
selectionSort(list_of_numbers, "a")
print('Sorted List:', list_of_numbers, '\n')

# descending
print('sorting in descending order')
print('Input List:', list_of_numbers)
selectionSort(list_of_numbers, "d")
print(f'Sorted descending list: {list_of_numbers}')
