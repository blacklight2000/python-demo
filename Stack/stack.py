class Stack():
    def __init__(self,a):
      self.a=a
    def pop(self):
        self.a.pop()
        return self
    def append(self,el):
        self.a.append(el)
        return self

a=[]
s=Stack(a)
s.append(1).append(2).append(3)
a
s.pop().pop().pop()
a

