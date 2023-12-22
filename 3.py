def RevPrint(N):
    if N < 10:
        print(N, end="")
    else:
        print(N % 10, end="")
        RevPrint(N // 10)

# Функция с проверкой ввода АОАОАОАОАОА КАК ЖЕ Я ЛЮБЛЮ ЭТОТ def АААААААА
def main():
    while True:
        try:
            N = int(input("Введите целое неотрицательное число: "))
            if N >= 0:
                RevPrint(N)
                break
            else:
                print("Число должно быть неотрицательным.")
        except ValueError:
            print("Ошибка! Введите целое число.")

# Опяяяяять запускаем программу через мои костыльные методы, простите
main()