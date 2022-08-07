# Name: Xu Yong Lin
# Admin no: 212033J
# Tutorial group: IT2153-01


# merge sort
def mergeSort(theList):
    if len(theList) <= 1:
        return theList
    else:
        # compute the midpoint
        mid = len(theList) // 2
        # print(f'mid index is: {mid}')

        # split the list and perform the recursive step
        leftHalf = mergeSort(theList[:mid])
        rightHalf = mergeSort(theList[mid:])

        # merge the 2 sorted sublists
        newList = mergeSortedLists(leftHalf, rightHalf)
        return newList


def mergeSortedLists(listA, listB):
    # create the new list and initialize the list markers
    # print('merging the 2 lists')
    # print(f'listA is {listA}')
    # print(f'listB is {listB}')

    newlist = []
    a = 0
    b = 0

    # merge the two lists together until one is empty
    while a < len(listA) and b < len(listB):
        if listA[a] < listB[b]:
            newlist.append(listA[a])
            a += 1
        else:
            newlist.append(listB[b])
            b += 1

    #  if listA contains more items, append remaining items to newList
    while a < len(listA):
        newlist.append(listA[a])
        a += 1

    # if listB contains more items, append remaining items to newList
    while b < len(listB):
        newlist.append(listB[b])
        b += 1

    # print(f'newlist is {newlist}')
    return newlist


#  test code
listofnumbers = [12, 7, 9, 24, 7, 29, 5, 3, 11, 7]
print(f'input list: {listofnumbers}')
merge_list = mergeSort(listofnumbers)
print(f'sorted list: {merge_list}')


list1 = [4, 1, 3, 10, 23, 31]
print(mergeSort(list1))  # >>> [1,3,4,10,23,31]
# print(list1) >>> [4,1,3,10,23,31]
