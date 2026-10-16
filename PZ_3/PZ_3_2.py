#Вариант 24. 2. 2. Даны координаты двух различных полей шахматной 
#доски х1, у1, х2, у2 (целые числа, лежащие в диапазоне 1-8). 
#Проверить истинность высказывания: «Ладья за один ход может перейти с одного поля на другое»

while True:

    x1 = (input("Введите первое значение х: "))
    while type(x1) != int:
        try:
            x1 = int(x1)
            if 1 <= abs(x1) <= 8:
                break
            else:
                print("Число должно быть от 1 до 8.")
                x1 = int(input("Введите первое значение х: "))
        except ValueError:
            print("Введено неверное значение.")
            x1 = (input("Введите первое значение х: "))

    x2 = (input("Введите второе значение х: "))
    while type(x2) != int:
        try:
            x2 = int(x2)
            if 1 <= abs(x2) <= 8:
                break
            else:
                print("Число должно быть от 1 до 8.")
                x2 = int(input("Введите второе значение х: "))
        except ValueError:
            print("Введено неверное значение.")
            x2 = (input("Введите второе значение х: "))

    y1 = (input("Введите первое значение y: "))
    while type(y1) != int:
        try:
            y1 = int(y1)
            if 1 <= abs(y1) <= 8:
                break
            else:
                print("Число должно быть от 1 до 8.")
                y1 = int(input("Введите первое значение y: "))
        except ValueError:
            print("Введено неверное значение.")
            y1 = (input("Введите первое значение y: "))

    y2 = (input("Введите второе значение y: "))
    while type(y2) != int:
        try:
            y2 = int(y2)
            if 1 <= abs(y2) <= 8:
                break
            else:
                print("Число должно быть от 1 до 8.")
                y2 = int(input("Введите второе значение y: "))
        except ValueError:
            print("Введено неверное значение.")
            y2 = (input("Введите второе значение y: "))

    if 1 <= x1 <= 8 and 1 <= x2 <= 8 and 1 <= y1 <= 8 and 1 <= y2 <= 8:
        if x1==x2 and y1==y2:
            print("Ладья осталась на месте.")
        else:
            if x1==x2 or y1==y2:
                print(True)
            else:
                print(False)
            break