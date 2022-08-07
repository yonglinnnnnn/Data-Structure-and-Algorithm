# Name: Xu Yong Lin
# Admin no: 212033J
# Tutorial group: IT2153-01

# linear search customer name
def linearSearch(arr, n, x):
    # O(n)
    list = []
    for i in range(0, n):
        if arr[i].customername.upper() == x.upper():
            list.append(i)  # inputs the index of the object
    return list


# binary search package name
def binarySearch(list, target):
    # log n
    result = []
    low = 0
    high = len(list) - 1
    while low <= high:
        mid = (low + high) // 2
        if target.upper() == list[mid].packagename.upper():
            result.append(mid)
            i = mid + 1
            # check left and right
            while i < len(list):
                if list[i].packagename.upper() == target.upper():
                    result.append(i)
                    i += 1
                else:
                    break
            i = mid - 1
            while i >= 0:
                if list[i].packagename.upper() == target.upper():
                    list.append(i)
                    i -= 1
                else:
                    break
            return result
        elif target.upper() < list[mid].packagename.upper():
            high = mid - 1
        else:  # thevalues[mid] < target
            low = mid + 1
    return result


# interpolation search customer name
def interpolationSearch(arr, arr_size, search):
    # log(logn)
    list = []
    lo = 0
    hi = arr_size - 1
    while (lo <= hi and search <= arr[hi].totalpax and search >= arr[lo].totalpax):
        if lo == hi:
            if arr[lo].totalpax == search:
                list.append(lo)
                # print(list)
                return list
        # inserting of checkpoint
        pos = lo + (((hi - lo) // (arr[hi].totalpax - arr[lo].totalpax)) * (search - arr[lo].totalpax))
        if arr[pos].totalpax == search:
            list.append(pos)
            k = pos + 1
            while k < len(arr):
                if arr[k].totalpax == search:
                    list.append(k)
                    k += 1
                else:
                    break
            k = pos - 1
            while k >= 0:
                if arr[k].totalpax == search:
                    list.append(k)
                    k -= 1
                else:
                    break
            return list
        elif arr[pos].totalpax < search:
            lo = pos + 1
        else:
            hi = pos - 1
    return list




