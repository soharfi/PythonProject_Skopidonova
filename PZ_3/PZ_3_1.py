#Вариант 24. 1. Дано четырехзначное число. Проверить истинность высказывания: 
# «Данное число читается одинаково слева направо и справа налево».

while True:
    try:
        x = int(input("Введите четырехзначное число: "))
        if x > 999 and x < 10000:
            first = x // 1000
            second = x // 100 % 10
            third = x // 10 % 10
            fourth = x % 10
            if first == fourth and second == third:
                print(True)
            else:
                print(False)
            break
    except ValueError:
        print("Введено неверное значение")
    except NameError:
        print("Число должно быть четырехзначным")