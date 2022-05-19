def PowerA234(a):
    b = a**2
    c = a**3
    d=a**4
    return (b,c,d)
print(PowerA234(4))

def season(u):
    if u in range(1,3) or u==12:
        return "зима"
    elif u in range(3,6):
        return "весна"
    elif u in range(6,9):
        return "лето"
    else:
        return "осень"
print(season(12))

# Банковский вклад '''
# Пользователь делает вклад в размере a рублей сроком на years лет под 10% годовых
# (каждый год размер его вклада увеличивается на 10%. Эти деньги прибавляются к сумме
# вклада, и на них в следующем году тоже будут проценты). Написать функцию bank,
# принимающая аргументы a и years, и возвращающую сумму, которая будет на счету
# пользователя.
def bank(z, years):
    for r in range(1, years+1):
        s=0
        s += (z + (z*0.1))
        after = s*r
    return after
print(bank(50000, 1825))

# Простые числа
# Написать функцию is_prime, принимающую 1 аргумент — число от 0 до 1000, и возвращающую
# True, если оно простое, и False - иначе.kkkkk
def is_prime(q):
    if q :
        return "True"

print(is_prime(110))
