class GameEntry:
    # create an entry with given name and score
    def __init__(self, name, score):
        self._name = name
        self._score = score

    # return the name of the person for this entry
    def get_name(self):
        return self._name

    # return the score of this entry
    def get_score(self):
        return self._score

    # return string representation of the entry
    def __str__(self):
        # eg '(Bob, 98)'
        return '({0} {1})'.format(self._name, self._score)

class Scoreboard:
    def __init__(self, capacity=10):
        self._board = [None] * capacity     # reserve space for future scores
        self._n = 0                         # number of actual entries

    # return entry at index k
    def __getitem__(self, k):
        return self._board[k]

    # return string representation of the high score list
    def __str__(self):
        return '\n'.join(str(self._board[j]) for j in range(self._n))

    # consider adding entry to high scores
    def add(self,entry):
        score = entry.get_score()
        # does new entry quality as a high score?
        # yes, if board is not full or score is higher than last entry
        qualified = self._n < len(self._board) or score > self._board[-1].get_score()

        # once the new entry is bigger than the last record in the board, it the following code will be executed
        if qualified:
            if self._n < len(self._board):      # no score drops from list
                self._n += 1                    # so overall number increases

            # shift lower scores rightward to make room for new entry
            j = self._n -1
            while j > 0 and self._board[j-1].get_score() < score:
                # 1. shift entry from j-1 to j
                self._board[j] = self._board[j-1]
                j -= 1 # 2. decrement j
            self._board[j] = entry
            # when done, add new entry


# test code
board = Scoreboard(5)
for e in (('Rob', 750), ('Mike', 1105), ('Rose', 590), ('Jill', 740), ('Jack', 510), ('Anna', 660), ('Paul', 720), ('Bob', 400)):
    ge = GameEntry(e[0], e[1])
    board.add(ge)
    print('After considering {0}, scoreboard is:'.format(ge))
    print(board, '\n')

