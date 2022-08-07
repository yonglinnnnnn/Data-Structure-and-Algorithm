# Name: Xu Yong Lin
# Admin no: 212033J
# Tutorial group: IT2153-01

def main():
    print(sumDigits(368))


def sumDigits(x):
    if x == 0:
        return 0
    else:
        return x % 10 + sumDigits(int(x / 10))


main()
