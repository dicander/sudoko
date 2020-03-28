def read_matrix():
    M = []
    for i in range(9):
        M.append((int(x) for x in input().split()))

    return M


def print_matrix(M):
    for row in M:
        print(" ".join((str(x) for x in row)))
    print()


def main():
    M = []
    while M!= None:
        M = read_matrix()
        print_matrix(M)
        try:
            input()
        except:
            return


main()