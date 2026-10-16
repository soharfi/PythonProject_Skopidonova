#Ввести двухзначное число. Если сумма цифр числа четная,
#то увеличить число на 2, в противном случае уменьшить на 2.

a = (input("Введите двухзначное число: "))
while type(a) != int:
    try:
        a = int(a)
        if 10 <= abs(a) <= 99:
            break
        else:
            print("Число должно быть двухзначным.")
            a = int(input("Введите двухзначное число: "))
    except ValueError:
        print("Введено неверное значение.")
        a = (input("Введите двухзначное число: "))

c = a//10
d = a%10
number = c+d
number = number%2
if number == 0:
    a = a*2
    print(a)
else:
    a = a/2
    print(a)