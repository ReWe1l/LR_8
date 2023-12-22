import random

# Ввод значений размеров списка и проверка ввода на корректность
def input_array_size():
    while True:
        try:
            size = int(input("Введите размер массива: "))
            if size > 0:
                return size
            else:
                print("Размер массива должен быть положительным числом.")
        except ValueError:
            print("Ошибка: Введите целое положительное число.")

# Генератор значений
def fill_array_random(array, size):
    for _ in range(size):
        array.append(random.randint(-10, 10))
    print("Сгенерирован массив:", array)

def calculate_average_positive(array):
    positive_elements = [x for x in array if x > 0]
    if len(positive_elements) > 0:
        return sum(positive_elements) / len(positive_elements)
    else:
        return 0

# Я ДЕЛАЛ ЭТУ ЧАСТЬ 2 ЧАСА
def main():
    X = []
    Y = []
    Z = []

    size_X = input_array_size()
    fill_array_random(X, size_X)

    size_Y = input_array_size()
    fill_array_random(Y, size_Y)

    size_Z = input_array_size()
    fill_array_random(Z, size_Z)

    average_X = calculate_average_positive(X)
    average_Y = calculate_average_positive(Y)
    average_Z = calculate_average_positive(Z)

    print("Среднее арифметическое положительных элементов массива X:", average_X)
    print("Среднее арифметическое положительных элементов массива Y:", average_Y)
    print("Среднее арифметическое положительных элементов массива Z:", average_Z)

# Запускаем программу, начиная с первой функции, создающей массивы
main()
