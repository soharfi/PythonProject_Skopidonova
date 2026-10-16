#Вариант 24. 1. Дано четырехзначное число. Проверить истинность высказывания: 
# «Данное число читается одинаково слева направо и справа налево».

x = (input("Введите четырехзначное число: "))
while type(x) != int:
    try:
        x = int(x)
        if 1000 <= abs(x) <= 9999:
            break
        else:
            print("Число должно быть четырехзначным.")
            x = int(input("Введите четырехзначное число: "))
    except ValueError:
        print("Введено неверное значение.")
        x = (input("Введите четырехзначное число: "))
    except NameError:
        print("Число должно быть четырехзначным")
        x = (input("Введите четырехзначное число: "))

if x > 999 and x < 10000:
    first = x // 1000
    second = x // 100 % 10
    third = x // 10 % 10
    fourth = x % 10
    if first == fourth and second == third:
        print(True)
    else:
        print(False)