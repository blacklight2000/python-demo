""" Function designed using generator """


def fibonacci():
    """ Function sequence starts from a = 0, b = 1 """
    a_value = 0
    b_value = 1
    i_value = 0
    while True:
        if i_value == 0:
            yield a_value
        elif i_value == 1:
            yield b_value
        else:
            a_value, b_value = b_value, a_value + b_value
            yield b_value
        i_value = i_value + 1

F = fibonacci()
assert([F.next() for _ in range(0, 5)] == [0, 1, 1, 2, 3])
assert(F.next() == 5)
