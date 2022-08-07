# Name: Xu Yong Lin
# Admin no: 212033J
# Tutorial group: IT2153-01

def last(n):
    return n[-1]


def sort(tuples):
    return sorted(tuples, key=last)


tobesorted = [(1, 7), (1, 3), (3, 4, 5), (2, 2)]
print(sort(tobesorted))
