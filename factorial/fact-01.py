In [1]: def fact():
    i = 0
    while True:
        if i == 0: yield 1
        if i == 1: yield 1
        if i > 1: yield i * (i - 1)
        i = i + 1
   ....:         

In [2]: f = fact()

In [3]: [f.next() for i in range(10)]
Out[3]: [1, 1, 2, 6, 12, 20, 30, 42, 56, 72]
