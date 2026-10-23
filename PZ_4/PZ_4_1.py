#вариант 24. Даны целые числа А и В ($A < B$). Вывести все целые числа от А до В включительно;
#при этом число А должно выводиться 1 раз, число А + 1 должно выводиться 2 раза и т. д.

a = input("Введите первое целое число: ")
while type(a) != int:
    try:
        a = int(a)
    except ValueError:
        print("Введено неверное значение.")
        a = input("Введите первое целое число: ")

b = input("Введите второе целое число: ")
while type(b) != int:
    try:
        b = int(b)
        if a < b:
            break
        else:
            print("Второе число должно быть больше первого")
            b = input("Введите второе целое число: ")
    except ValueError:
        print("Введено неверное значение.")
        b = input("Введите второе целое число: ")

num = a
counter = 1

while num <= b:
    i = 0
    while i < counter:
        print(num, end="")
        i += 1
    num += 1
    counter += 1

print()