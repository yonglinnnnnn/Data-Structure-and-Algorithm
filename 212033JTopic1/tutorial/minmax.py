# question 1
def minmax(data):
    small = big = data[0]  # assuming data is non-empty
    for n in data:
        if n < small:
            small = n
        elif n > big:
            big = n
    return small, big


nums = [3, 6, 9, 12, 25, 11, 26, 80]
a, b = minmax(nums)
print('small = ', a)
print(minmax(nums))
