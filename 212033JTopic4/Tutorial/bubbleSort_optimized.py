# Name: Xu Yong Lin
# Admin no: 212033J
# Tutorial group: IT2153-01


def bubbleSort_optimized(theSeq):
    n = len(theSeq)

    # perform n - 1 bubble operations on the sequence
    for i in range(n - 1, 0, - 1):
        # set boolean variable to check occurrence of swapping in inner loop
        noSwap = True

        # bubble the largest item to the end
        for j in range(i):
            if theSeq[j] > theSeq[j + 1]:
                # swap j and j+1 item
                theSeq[j], theSeq[j + 1] = theSeq[j + 1], theSeq[j]

                # set boolean variable value if swapping occured
                noSwap = False

        # exit the loop if no swapping occured in the previous pass
        if noSwap:
            break


data = [-2, 45, 0, 11, -9]
print(f'Before sort: {data}')
bubbleSort_optimized(data)
print(f'After sort: {data}')
