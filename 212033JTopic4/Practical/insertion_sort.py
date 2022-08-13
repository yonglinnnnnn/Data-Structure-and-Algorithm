# Name: Xu Yong Lin
# Admin no: 212033J
# Tutorial group: IT2153-01

# enhancement: sorting the list in both ascending and descending

def insertionSort(theSeq, ascdec):
    n = len(theSeq)
    # Starts with the first item as the only sorted entry.
    for i in range(1, n):
        # Save the value to be positioned
        value = theSeq[i]
        # Find the position where value fits in the
        # ordered part of the list.
        pos = i
        if ascdec.lower() == 'a':
            while pos > 0 and value < theSeq[pos - 1]:
                # Shift the items to the right during the search
                theSeq[pos] = theSeq[pos - 1]
                pos -= 1
            # Put the saved value into the open slot.
            theSeq[pos] = value

            # for understanding purposes
            print(f'Pass : {i}      {theSeq}')
        elif ascdec.lower() == 'd':
            while pos > 0 and value > theSeq[pos - 1]:
                # Shift the items to the right during the search
                theSeq[pos] = theSeq[pos - 1]
                pos -= 1
            # Put the saved value into the open slot.
            theSeq[pos] = value

            # for understanding purposes
            print(f'Pass : {i}      {theSeq}')
        else:
            print('Enter either ascending (a) or descending (d) only')


# Test codes
list_of_numbers = [10, 51, 2, 18, 4, 31, 13, 5, 23, 64, 29]
# ascending
print('===Ascending===')
print('Pass : 0     ', list_of_numbers)
insertionSort(list_of_numbers, 'a')
print()
print('Sorted List:', list_of_numbers, '\n')

# descending
list_of_numbers2 = [10, 15, 2, 81, 4, 31, 13, 92]
print('===Descending===')
print('Pass : 0     ', list_of_numbers2)
insertionSort(list_of_numbers2, 'd')
print()
print('Sorted List:', list_of_numbers2)

