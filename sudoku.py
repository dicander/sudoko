import collections

ROWS = []
COLUMNS = []
SQUARES = []
FIND_MY_SQUARE = []
POSSIBLE = set(range(1, 10))
DBG = True


def read_matrix():
    """Reads a 9x9 sudoku sized matrix where we can trust input to be integers"""
    M = []
    for i in range(9):
        M.append([int(x) for x in input().split()])
    return M


def print_matrix(M):
    for row in M:
        print(" ".join((str(x) for x in row)))
    print()


def init():
    """Initialize the global constant arrays."""
    for y in range(9):
        vc = set()
        vs = set()
        for x in range(9):
            vc.add((x, y))
            vs.add((y, x))
        ROWS.append(vs)
        COLUMNS.append(vc)
    for i in range(9):
        FIND_MY_SQUARE.append([-1 for x in range(9)])
    for y in range(9):
        for x in range(9):
            FIND_MY_SQUARE[y][x] = 3 * (y // 3) + x // 3
    if False:
        print("What are you doing?")
        print(FIND_MY_SQUARE)
    for i in range(9):
        SQUARES.append(set())
    for y in range(9):
        for x in range(9):
            SQUARES[FIND_MY_SQUARE[y][x]].add((y, x))
    if False:
        print(ROWS)
        print(COLUMNS)
        print(SQUARES)


def solve(M):
    if DBG:
        print(type(M))
        print(M)
    d = collections.deque()
    for y in range(9):
        for x in range(9):
            if M[y][x] == 0:
                d.appendleft((y, x))
    my_rows = [{M[y][x] for x in range(9)} - {0} for y in range(9)]
    my_columns = [{M[y][x] for y in range(9)} - {0} for x in range(9)]
    my_squares = [{M[y][x] for (y, x) in SQUARES[i]} - {0} for i in range(9)]
    zeroes_in_rows = [{(y, x) for x in range(9) if M[y][x] == 0} for y in range(9)]
    zeroes_in_columns = [{(y, x) for y in range(9) if M[y][x] == 0} for x in range(9)]
    zeroes_in_squares = [{pos for pos in SQUARES[i] if M[pos[0]][pos[1]] == 0} for i
                         in range(9)]
    if DBG:
        print(my_rows)
    while d:
        if DBG:
            print(len(d))
        y, x = d.pop()
        if M[y][x] != 0:
            continue
        candidates = POSSIBLE ^ (my_rows[y] | my_columns[x]
                                 | my_squares[FIND_MY_SQUARE[y][x]])
        if len(candidates) == 1:
            new_digit = candidates.pop()
            M[y][x] == new_digit
            my_rows[y].add(new_digit)
            my_columns[x].add(new_digit)
            current_square = FIND_MY_SQUARE[y][x]
            my_squares[current_square].add(new_digit)
            zeroes_in_rows[y] -= {(y, x)}
            zeroes_in_columns[x] -= {(y, x)}
            zeroes_in_squares[current_square] -= {(y, x)}
            possibly_affected = zeroes_in_squares[current_square] \
                                 | zeroes_in_rows[y] \
                                 | zeroes_in_columns[x]
            d.extend(possibly_affected)
        else:
            d.appendleft((y, x))
    print_matrix(M)
    print()

def main():
    init()
    M = []
    while M != None:
        M = read_matrix()
        solve(M)
        # print_matrix(M)
        try:
            input()
        except:
            return


main()
