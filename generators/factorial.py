def factorial():
    i=0
    n=1
    while True:
        if i == 0:
            yield n
        elif i == 1:
            yield n
        else:
            n=n*i
            yield n
        i=i+1

f=factorial()
[f.next() for i in range(0,5)]

