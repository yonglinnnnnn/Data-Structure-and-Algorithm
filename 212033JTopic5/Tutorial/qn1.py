# Name: Xu Yong Lin
# Admin no: 212033J
# Tutorial group: IT2153-01

def main():
    print(sum(10))


def sum(x):
    if x == 1:
        return 1
    else:
        # assuming x >= 1
        # complete the function recursively
        return x + sum(x - 1)


main()
