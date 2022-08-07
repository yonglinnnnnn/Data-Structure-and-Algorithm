# Name: Xu Yong Lin
# Admin no: 212033J
# Tutorial group: IT2153-01

# additional function: set pivot as the median value
def median(L, low, high):
    mid = (low + high - 1) // 2
    a = L[low]
    b = L[mid]
    c = L[high - 1]

    # median: b
    # a smaller than b, b smaller than c
    if a <= b and b <= c:
        return b, mid
    # c is smaller than b, b is smaller than a
    if c <= b and b <= a:
        return b, mid

    # median: c
    # a is smaller than c, c is smaller than a
    if a <= c and c <= b:
        return c, high - 1
    # b is smaller than c, c is smaller than a
    if b <= c and c <= a:
        return c, high - 1

    # median: a (other cases)
    return a, low


# quick sort
#  sorts a python list in ascending order using the quick sort algo
def quickSort(theList):
    n = len(theList)
    recQuickSort(theList, 0, n - 1)


def recQuickSort(theList, first, last):
    result = 0
    # check the base case (range is trivially sorted)
    if first >= last:
        return 0
    else:
        # partition the list and obtain the pivot position
        pos, result = partitionSeq(theList, first, last)

        # repeat the process on the two sublists
        result += recQuickSort(theList, first, pos)
        result += recQuickSort(theList, pos + 1, last)
    return result


def partitionSeq(theList, first, last):
    # save a copy of the pivot value
    result = 0
    pivot, pidx = median(theList, first, last)
    print(f'pivot: {pivot}, pidx: {pidx}')
    theList[first], theList[pidx] = theList[pidx], theList[first]
    i = first + 1

    for j in range(first, last, 1):
        result += 1
        if theList[j] < pivot:
            theList[i], theList[j] = theList[j], theList[i]
            i += 1

    theList[first], theList[i - 1] = theList[i - 1], theList[first]
    return i - 1, result


# test code
listofnumbers = [12, 7, 9, 24, 7, 29, 5, 3, 11, 7]
print(f'input list: {listofnumbers}')
quickSort(listofnumbers)
print(f'sorted list: {listofnumbers}')
