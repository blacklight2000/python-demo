""" Factorial function designed using generator """


def factorial():
    """ Factorial starts from 0! = 1 """
    i_value = 0
    n_value = 1
    while True:
        if i_value == 0:
            yield n_value
        elif i_value == 1:
            yield n_value
        else:
            n_value = n_value * i_value
            yield n_value
        i_value = i_value + 1

if __name__ == "__main__":
    F = factorial()
    assert([F.next() for _ in range(0, 5)] == [1, 1, 2, 6, 24])
    F = factorial()
    assert([F.next() for _ in range(0, 6)] == [1, 1, 2, 6, 24, 120])
    assert(F.next() == 720)
