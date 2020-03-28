N_CARS = 23
NAME = "MACBOOK PRO"
log = []


def f(v, i):
    v.append(2)
    i += 23
    print(v, i)


def main():
    v = [1]
    i = 3000
    f(v,i)
    print(v, i)


def g():
    global N_CARS
    print(N_CARS)
    N_CARS += 1
    log.append(23)


def h(v=None):
    if v is None:
        v = []
    print(v)
    v.append(1)
    print(v)


a = 42
b = 42
if a == b == True:
    print("Hej!")

for x in range(10):
    print(h())
g()
main()