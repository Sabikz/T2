#1) Простые числа
#Написать функцию is_prime, принимающую 1 аргумент — число от 0 до 1000,
# и возвращающую True, если оно простое, и False - иначе.
def is_prime(q):
    for i in range(2, q):
        if q%i==0:
            return "False"
        else:
            return "True"
print(is_prime(11))

#2) Правильная дата
#Написать функцию date, принимающую 3 аргумента — день, месяц и год. Вернуть True,
# если такая дата есть в нашем календаре, и False иначе.

def date(day, month, year):
    if day <= 0 or month <= 0 or year < 0:
        return False
    else:
        months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if year % 4 == 0:
            months[1] = 29
        if day <= months[month - 1]:
            if month <= 12:
                return True
        return False
print(date(35, 12, 2022))

#3) От 0 до n
#Написать функцию, принимающую одно целочисленное значение
# и возвращающую сумму целых чисел от 0 до этого значения включительно.
def num(t):
    s = 0
    for i in range (0, t+1):
        s+= i
    return s
print(num(56))

#4) Максимум и минимум
#Написать функцию, принимающую один список состоящий из целочисленных элементов.
# Вернуть максимальное и минимальное значении в списке

def printStatistics(L):
    for i in range(len(L)):
        return max(L), min(L)
print(printStatistics([5, 0.8, 677]))






