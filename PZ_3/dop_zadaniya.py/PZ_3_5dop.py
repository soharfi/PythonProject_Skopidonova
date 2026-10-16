#Дано два числа. Если их сумма кратна 5, то прибавить 1, иначе вычесть 2.

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

summa = a+b
if summa%5 == 0:
    summa = summa+1
    print(summa)
else:
    summa = summa-2
    print(summa)
