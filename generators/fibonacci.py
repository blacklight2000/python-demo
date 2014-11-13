def fibonacci():
   a=0
   b=1
   i=0
   while True:
     if i == 0:
       yield a
     elif i == 1:
       yield b
     else:
       a,b=b,a+b
       yield b
     i=i+1

f= fibonacci()
[f.next for i in range(0,5)]

