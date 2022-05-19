# 20
import math
A = float(input("A: "))
B = float(input("B: "))
C = float(input("C: "))
AB = abs(A - B)
AC = abs(A - C)
if AB < AC:
    print('Точка В ближе к А. Расстояние равно %.2f' % AB)
if AC < AB:
    print('Точка C ближе к А. Расстояние равно %.2f' % AC)
if AB==AC:
    print('Точка В и С равны к А.Расстояние равно %.2f' % AB)

#21

x=int(input("x:"))
y=int(input("y:"))
if x==0 and y==0:
    print("0")
elif x == 0:
    print("1")
elif y==0:
    print("2")
else:
    print("3")

#22

x1 = int(input("x1:"))
y1 = int(input("y1:"))
if x1 >0 and y1 > 0:
    print("I")
elif x1 < 0 and y1 > 0:
    print("II")
elif x1 < 0 and y1 < 0:
    print("III")
else:
    print("IV")

#23
ax = int(input("ax:"))
bx = int(input("bx:"))
cx = int(input("cx:"))
ay = int(input("ay:"))
by = int(input("by:"))
cy = int(input("cy:"))
dx = int()
dy=int()
if ax ==bx:
    dx==cx
elif ax==cx:
    dx==bx
else:
    dx==ax
if ay==by:
    dy==cy
elif ay==cy:
    dy==by
else:
    dy==ay
print(dx, dy)

#24
x2 = float(input("x2:"))
fx2 = float()
if x2>0: fx = 2*math.sin(x2)
elif x2<=0: fx2 = 6-x2
else: fx2=0
print(fx2)

#25
fx3 = int()
x3= int(input("x3:"))
for x3 in range (-5,10):
    if x3<-2 or x3>2:
        fx3 = 2*x3
    else:
        fx3 = -3*x3
print(fx3)

#26
for x4 in range(-2,7):
    if x4 <= 0:
        fx4 = -x4
    elif x4 < 2:
        fx4 = x4 * x4
    else:
        fx4 = 4
    print("x = {0} : f(x) = {1}".format(x4,fx4))

# 27

x5 = int()
fx5 = int()
while x5 < 5:
    x_floor = math.floor(x5)
    if x5 <= 0:
        fx5 = 0
    elif x_floor%2 == 0:
        fx5 = 1
    else:
        fx5 = -1
    print("x = {0} : f(x) = {1}".format(x5,fx5))
    x5 += .5


