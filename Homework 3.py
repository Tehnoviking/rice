import math
from math import factorial,log
#примеры
#1
n = 0
eps = 0.0001
summa = 0
part = 1
x = float(input('set:'))
x = round(math.radians(x), 2)

while abs(part) > eps:
    part = ((-1)**n)*((x**(2*n+1))/factorial(2*n+1))
    summa += part
    n += 1
print(f'sin:{summa}')
#2
n = 0
eps = 0.0001
summa = 0
part = 1
x = float(input('set:'))
x = round(math.radians(x), 2)

while abs(part) > eps:
    part = ((-1)**n)*((x**(2*n))/factorial(2*n))
    summa += part
    n += 1
print(f'cos:{summa}')

# 3
k = 0
m = float(input('set m:'))
x = float(input('set x:'))
eps = 0.0001
part_2 = 1
summa = 0
while abs(part_2) > eps:
    part_2 = ((m**k)*(log(x+1)**k))/(factorial(k))
    summa += part_2
    k += 1
print(summa)

#4
part_3=1
x=float(input('set x:'))
n=int(input('set n:'))
eps=0.0001
summa=0
while abs(part_3)>eps:
    part_3=(x**n)/factorial(n)
    summa+=part_3
    n+=1
print(summa)

#5
x=float(input('set x:'))
n=float(input('set n:'))
part_4=0
eps=0.0001
while abs(part_4)>eps:
    part_4=((-1)**(n-1))*((x**n)/n)
    summa+=part_4
    n+=1
print(summa)

#Написать filter  с лямбда-функцией определяющей число чётное/нечётное.
print(list(filter(lambda x:x%2==0,[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])))
#Дан список. Сделать список с помощью функции map, которая переводит каждое число из исходного списка в строку
print(list(map(lambda x: str(x),[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,55])))
#С помощью функции filter отфильтровать из исходного списка строк только те строки, которые являются палиндромами. Палиндром - в обе стороны читается одинаково. ‘abccba’ - палиндром например
print(list(filter(lambda x: x==x[::-1],['abccba','madam','dama','music'])))

#Декорирование
def decorate_new(func):
    import time
    def wrapper(*args,**kwargs):
        t=time.clock()
        res=func(*args,**kwargs)
        print(func.__name__,time.clock()-t)
        return(res)
    return wrapper


@decorate_new
def str(str):
    return(str)
print(str('Privet Olyga'))
