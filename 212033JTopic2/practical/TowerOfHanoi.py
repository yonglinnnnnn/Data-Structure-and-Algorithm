# Name: Xu Yong Lin
# Admin no: 212033J
def main():
    # set up some initial values
    num_discs = 3 # no of discs to move
    from_peg = 1  # peg to move from
    to_peg = 3    # peg to move to
    temp_peg = 2  # temporary peg
    # play the game
    move_discs(num_discs, from_peg, to_peg, temp_peg)
    print('All the pegs are moved!')
    print()

# algorithm to move the discs
def move_discs(num, from_peg, to_peg, temp_peg):
    if num > 0:
        move_discs(num - 1, from_peg, temp_peg, to_peg)     #recursive
        print("Move a disc from peg", from_peg, "to peg", to_peg)
        move_discs(num - 1, temp_peg, to_peg, from_peg)     #recursive, call the function again

main()
print('*****')


# alternative method
def hanoi(n, source, destination, temp):
    if n == 1:
        print("Move disk 1 from source", source, 'to destination', destination)
        return
    hanoi(n-1, source, temp, destination)
    print('Move disk', n,'from source', source, 'to destination', destination)
    hanoi(n-1, temp, destination, source)


hanoi(3, 'A', 'C', 'B')
