""" Example function decorator """


def squareit(func):
    """ decorator for the wrapper """
    def wrap(*args, **kwargs):
        """ wrapper around the function, whatever the function is """
        x_val = func(*args, **kwargs)
        return x_val * x_val
    return wrap

@squareit
def doubles(x_val):
    """ original function """
    return 2 * x_val


if __name__ == "__main__":
    assert(doubles(3) == 36)
