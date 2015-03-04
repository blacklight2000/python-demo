""" Example class decorator """


class CallCount:
    """ class decorator """
    def __init__(self, func):
        self.count = 0
        self.func = func
 
    def __call__(self, *args, **kwargs):
        self.count += 1
        return self.func(*args, **kwargs)

@CallCount
def hello(name):
    """ hello is the function to be wrapped by the decorator """
    print('hello, {}'.format(name))
