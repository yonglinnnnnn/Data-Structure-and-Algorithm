# Name: Xu Yong Lin
# Admin no: 212033J
# Tutorial group: IT2153-01


def recBinarySearch(target, theValues, first, last):
    # if the sequence of values cannot be subdivided further
    # we r done

    # base case
    if first > last:
        return False
    else:
        # find the midpoint of the sequence
        mid = (last + first) // 2

        # does the element at the midpoint contain the target?
        if theValues[mid] == target:
            return True

        # or does the target precede the element at the midpoint?
        elif target < theValues[mid]:
            return recBinarySearch(target, theValues, first, mid-1)

        # or does the target follows the element at the midpoint?
        else:
            return recBinarySearch(target, theValues, mid+1, last)


# test code
sortedListOfNum = [1, 2, 7, 10, 18, 25, 30, 33, 42, 56, 61, 70, 73, 88]
print(recBinarySearch(10, sortedListOfNum, 0, len(sortedListOfNum)))
print(recBinarySearch(73, sortedListOfNum, 0, len(sortedListOfNum)))
