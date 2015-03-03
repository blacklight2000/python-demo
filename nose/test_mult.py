# from unittest.runner import _WritelnDecorator

def mult(x,y):
  return x*y

def test_mult_4_5():
  assert(mult(4,5)==20)

def test_mult_4_6():
  assert(mult(4,6)==24)

