class Case1:
    msg = "Input to fibonacci sequence must be a non-negative integer"
    @classmethod
    def fibonacci(cls,n):
        try:
           if (n<0) or (not isinstance(n,int)): raise IOError({"message": cls.msg})
           f = [0,1]
           if n < 2: return f[n]
           else: return cls.fibonacci(n-1)+cls.fibonacci(n-2)
        except IOError,e:
           details = e.args[0]
           return details['message']


class Case2:
    msg = "Input to fibonacci sequence must be a non-negative integer"
    @classmethod
    def fibonacci(cls,n):
        try:
           if (n <0) or (not isinstance(n,int)): raise IOError({"message": cls.msg})
           f = [0,1]
           if n <2: return f[n]
           else:
              for i in range(1,n):
                 f[0], f[1] = f[1],f[0]+f[1]
              return f[1]
        except IOError,e:
           details = e.args[0]
           return details['message']
    
