class Case1:
    @classmethod
    def fibonacci(cls,n):
        f = [0,1]
        if n < 2: return f[n]
        else: return cls.fibonacci(n-1)+cls.fibonacci(n-2)


class Case2:
    @classmethod
    def fibonacci(cls,n):
        f = [0,1]
        if n <2: return f[n]
        else:
            for i in range(1,n):
                f[0], f[1] = f[1],f[0]+f[1]
            return f[1]



