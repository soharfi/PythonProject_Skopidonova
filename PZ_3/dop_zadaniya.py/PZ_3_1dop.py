#1. Ввести 2 числа. Если их произведение отрицательно, 
#умножить его на 8, в противном случае увеличить его в 1.5 раза.

a = int(input("Введите первое число: "))
while type(a) != int:
    try:
        a = int(a)
    except ValueError:
        print("Введено неверное значение.")
        a = (input("Введите первое число: "))

b = int(input("Введите второе число: "))
while type(b) != int:
    try:
        b = int(b)
    except ValueError:
        print("Введено неверное значение.")
        b = (input("Введите второе число: "))

c = a*b

if c<0:
    c = c*8
    print(c)
else:
    c = c*1.5
    print(c)