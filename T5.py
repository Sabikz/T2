#1) Даны два словаря:
dictionary_1 = {'a': 300, 'b': 400}
dictionary_2 = {'c': 500, 'd': 600}
# Объедините их в один при помощи встроенных функций языка Python.
c = dictionary_1 | dictionary_2
print(c)

#2) Создайте словарь, в котором ключами будут числа от 1 до 10,
# а значениями эти же числа, возведенные в куб.
d = dict()
for i in range (1,11):
    d[i]=i**3
print(d)



#3) Даны два списка одинаковой длины. Необходимо создать из них словарь таким образом,
# чтобы элементы первого списка были ключами, а элементы второго — соответственно значениями нашего словаря.
keys = ['red', 'green', 'blue']
values = ['#FF0000','#008000', '#0000FF']
f = dict(zip(keys, values))
print(f)