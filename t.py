

# Выводить на экран от -10 до +10
# Выводить на экран от +10 до -10
# Вывести все цифры от 1 до 100 через *2 (1, 2, 4, 8, 16 и т.д.)
# Посчитать сумму цифр от 1 до 25

def func(a):
    if a == 11:
        return
    print(a)
    return func(a+1)
func(-10)

def func1(b):
    if b==-11:
        return
    print(b)
    return func1(b-1)
func1(10)

def func2(c):
    if c > 101:
        return
    print(c)
    return func2(c*2)
func2(1)

def func3(d, s):
    if d == 25:
        return
        print(s)
    return func3(d+1), s+d
func3(1,0)

