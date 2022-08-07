# Name: Xu Yong Lin
# Admin no: 212033J
# Tutorial group: IT2153-01

# additional function: set pivot as the median value

# quick sort
#  sorts a python list in ascending order using the quick sort algo
def quickSort(theList):
    n = len(theList)
    recQuickSort(theList, 0, n-1)


def recQuickSort(theList, first, last):
    # check the base case (range is trivially sorted)
    if first >= last:
        return

    else:
        # partition the list and obtain the pivot position
        pos = partitionSeq(theList, first, last)
        print(f'pivot index is: {pos}')
        # repeat the process on the two sublists
        recQuickSort(theList,first, pos-1)
        recQuickSort(theList, pos+1, last)


def partitionSeq(theList, first, last):
    # save a copy of the pivot value
    pivot = theList[first]
    print(f'partitionSeq this list: {theList}')
    print(f'first = {first}    &      last = {last}')
    print(f'pivot is {pivot}')

    # find the pivot position and move the elements around it
    left = first + 1        # will scan leftward
    right = last            # will scan rightward

    while left <= right:
        # scan until reaches value equal or larger than pivot (or right marker)
        while left <= right and theList[left] < pivot:
            left += 1
            # print(left)

        # scan until reaches value equal or smaller than pivto (or left marker)
        while left <= right and theList[right] > pivot:
            right -= 1

        # scans did not strictly cross
        if left <= right:
            # swap values
            theList[left], theList[right] = theList[right], theList[left]
            #shrink range (recursion: progress towards base case)
            left += 1
            right -= 1

    # put the pivot in the proper position (marked by the right index)
    theList[first], theList[right] = theList[right], pivot
    # return the index position of the pivot value
    return right

# test code
listofnumbers = [12,7,9,24,7,29,5,3,11,7]
print(f'input list: {listofnumbers}')
quickSort(listofnumbers)
print(f'sorted list: {listofnumbers}')

