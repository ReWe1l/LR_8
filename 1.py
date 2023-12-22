def TriangleParameters(a):
    P = a * 3
    S = (a ** 2) * ((3 ** 0.5) / 4)
    return P, S

def get_input():
    while True:
        try:
            num = int(input("Введите длину стороны треугольника: ",))
            return num
        except ValueError:
            print("Ошибка: Введите число.")

a1 = get_input()
a2 = get_input()
a3 = get_input()

otvet1 = TriangleParameters(a1)
otvet2 = TriangleParameters(a2)
otvet3 = TriangleParameters(a3)

print(otvet1, otvet2, otvet3)