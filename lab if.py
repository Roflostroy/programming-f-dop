#1
print('Задание 1')
x, y = int(input("Введите x: ")), int(input("Введите y: "))
if x**2 + y**2 <= 10**2:
    print('Точка внутри круга')
else:
    print('Точка вне круга')

#2
print('Задание 2')
x, y = int(input("Введите x: ")), int(input("Введите y: "))
R, N = int(input("Введите радиус R: ")), int(input("Введите смещение N: "))
if (x - N)**2 + y**2 <= R**2:
    print('Точка внутри круга')
else:
    print('Точка вне круга')
