def read_matrix():
    M = []
    for i in range(9):
        M.append((int(x) for x in input().split()))

    return M


def print_matrix(M):
    for row in M:
        print(" ".join((str(x) for x in row)))


def testio():
    M = []
    while M!= None:
        print_matrix(M)
        M = read_matrix()
        if input() == None:
            return


testio()