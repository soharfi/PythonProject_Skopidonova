#2. Вести число. Если оно четное, разделить его на 4, если нечетное - умножить на 5.

a = int(input("Введите число: "))
while type(a) != int:
    try:
        a = int(a)
    except ValueError:
        print("Введено неверное значение.")
        a = (input("Введите число: "))

if a % 2 == 0:
    a = a/4
    print(a)
else:
    a = a*5
    print(a)