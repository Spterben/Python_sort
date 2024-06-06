import random
import time
import matplotlib.pyplot as plt
import numpy as np

def measure_sorting_time(sorting_func, data):
    """Измеряет время выполнения функции сортировки."""
    start_time = time.time()  # Засекаем начальное время
    sorting_func(data)  # Вызываем функцию сортировки
    elapsed_time = time.time() - start_time  # Вычисляем прошедшее время
    return elapsed_time  # Возвращаем затраченное время

def generate_random_data(size):
    """Генерирует список случайных чисел заданного размера."""
    return [random.randint(1, 1000) for _ in range(size)]  # Генерируем список случайных чисел

def plot_performance(data_sizes, *sorting_funcs):
    """Строит график производительности различных алгоритмов сортировки."""
    plt.xlabel('Количество элементов')  # Задаем подпись оси X
    plt.ylabel('Время (секунды)')  # Задаем подпись оси Y
    plt.title('Производительность (среднее время из {} повторов)'.format(repetitions))  # Задаем заголовок графика

    for sorting_func in sorting_funcs:  # Для каждой функции сортировки
        avg_times = []  # Создаем пустой список для хранения средних времен
        for size in data_sizes:  # Для каждого размера данных
            total_time = sum(measure_sorting_time(sorting_func, generate_random_data(size)) for _ in range(repetitions))  # Суммируем время выполнения функции сортировки repetitions раз
            avg_times.append(total_time / repetitions)  # Добавляем среднее время в список
        plt.plot(data_sizes, avg_times, label=sorting_func.__name__)  # Строим график среднего времени выполнения

        trend = np.polyfit(data_sizes, avg_times, 2)  # Вычисляем коэффициенты для линии тренда
        formula = f"{trend[0]:.2f}x^2 + {trend[1]:.2f}x + {trend[2]:.2f}"  # Формула квадратичной функции для линии тренда
        label_x = min(data_sizes) + (max(data_sizes) - min(data_sizes)) * 0.6  # Размещаем текст ближе к правому краю графика
        label_y = max(avg_times) * 0.9  # Размещаем текст ближе к верхнему краю графика
        plt.text(label_x, label_y, f"{sorting_func.__name__}: {formula}", fontsize=8)  # Выводим формулу линии тренда на график

    plt.legend()  # Выводим легенду
    plt.show()  # Отображаем график

repetitions = 10  # Количество повторений для усреднения времени выполнения
data_sizes = list(range(100, 1000, 100))  # Размеры данных для тестирования алгоритмов

def bubble_sort(nums):
    """Сортировка списка методом пузырька."""
    n = len(nums)  # Вычисляем длину списка
    for i in range(n):  # Для каждого элемента списка
        for j in range(0, n-i-1):  # Для каждого элемента, который нужно проверить
            if nums[j] > nums[j + 1]:  # Если текущий элемент больше следующего
                nums[j], nums[j + 1] = nums[j + 1], nums[j]  # Меняем их местами
        else:
            break  # Если не было перестановок, завершаем сортировку

def selection_sort(nums):
    """Сортировка списка методом выбора."""
    for i in range(len(nums)):  # Для каждого элемента списка
        min_index = i  # Предполагаем, что текущий элемент минимальный
        for j in range(i + 1, len(nums)):  # Для каждого элемента после текущего
            if nums[j] < nums[min_index]:  # Если текущий элемент меньше предполагаемого минимального
                min_index = j  # Обновляем индекс минимального элемента
        nums[i], nums[min_index] = nums[min_index], nums[i]  # Меняем местами текущий элемент и минимальный

def insertion_sort(nums):
    """Сортировка списка методом вставки."""
    for i in range(1, len(nums)):  # Для каждого элемента начиная со второго
        key = nums[i]  # Запоминаем текущий элемент
        j = i - 1  # Начинаем сравнивать с предыдущим элементом
        while j >= 0 and key < nums[j]:  # Пока не достигли начала списка и текущий элемент меньше предыдущего
            nums[j + 1] = nums[j]  # Сдвигаем предыдущий элемент вправо
            j -= 1  # Переходим к следующему предыдущему элементу
        nums[j + 1] = key  # Вставляем текущий элемент на правильную позицию

def heapify(nums, heap_size, root_index):
    """Преобразует список в кучу."""
    largest = root_index  # Предполагаем, что наибольший элемент находится в корне
    left_child = (2 * root_index) + 1  # Индекс левого потомка
    right_child = (2 * root_index) + 2  # Индекс правого потомка

    if left_child < heap_size and nums[left_child] > nums[largest]:  # Если индекс левого потомка в пределах кучи и он больше текущего наибольшего элемента
        largest = left_child  # Обновляем индекс наибольшего элемента

    if right_child < heap_size and nums[right_child] > nums[largest]:  # Если индекс правого потомка в пределах кучи и он больше текущего наибольшего элемента
        largest = right_child  # Обновляем индекс наибольшего элемента

    if largest != root_index:  # Если наибольший элемент не в корне
        nums[root_index], nums[largest] = nums[largest], nums[root_index]  # Меняем их местами
        heapify(nums, heap_size, largest)  # Продолжаем преобразование до тех пор, пока куча не будет удовлетворять свойству кучи

def heap_sort(nums):
    """Сортировка списка методом сортировки кучей."""
    n = len(nums)  # Длина списка
    for i in range(n // 2 - 1, -1, -1):  # Превращаем список в кучу
        heapify(nums, n, i)  # Преобразуем поддерево с корнем в i в кучу
    for i in range(n - 1, 0, -1):  # Для каждого элемента в куче
        nums[i], nums[0] = nums[0], nums[i]  # Меняем его с последним элементом
        heapify(nums, i, 0)  # Преобразуем кучу

def merge(left_list, right_list):
    """Слияние двух отсортированных списков."""
    sorted_list = []  # Создаем пустой список для хранения результата слияния
    left_index = right_index = 0  # Устанавливаем индексы для прохода по обоим спискам
    while left_index < len(left_list) and right_index < len(right_list):  # Пока не достигнут конец хотя бы одного списка
        if left_list[left_index] < right_list[right_index]:  # Если элемент из левого списка меньше элемента из правого списка
            sorted_list.append(left_list[left_index])  # Добавляем элемент из левого списка в результирующий список
            left_index += 1  # Переходим к следующему элементу левого списка
        else:
            sorted_list.append(right_list[right_index])  # Добавляем элемент из правого списка в результирующий список
            right_index += 1  # Переходим к следующему элементу правого списка

    sorted_list.extend(left_list[left_index:])  # Добавляем оставшиеся элементы из левого списка
    sorted_list.extend(right_list[right_index:])  # Добавляем оставшиеся элементы из правого списка

    return sorted_list  # Возвращаем результирующий список

def merge_sort(nums):
    """Сортировка списка методом слияния."""
    if len(nums) <= 1:  # Если длина списка меньше или равна 1
        return nums  # Возвращаем сам список

    mid = len(nums) // 2  # Находим середину списка
    left_list = merge_sort(nums[:mid])  # Рекурсивно сортируем левую половину списка
    right_list = merge_sort(nums[mid:])  # Рекурсивно сортируем правую половину списка

    return merge(left_list, right_list)  # Возвращаем результат слияния отсортированных половин

def partition(nums, low, high):
    """Разделение списка на две части относительно опорного элемента."""
    pivot = nums[(low + high) // 2]  # Определяем опорный элемент
    i = low - 1  # Устанавливаем индекс, который будет увеличиваться после каждого меньшего или равного опорному элементу
    j = high + 1  # Устанавливаем индекс, который будет уменьшаться после каждого большего или равного опорному элементу

    while True:  # Бесконечный цикл
        i += 1  # Переходим к следующему элементу
        while nums[i] < pivot:  # Пока элемент меньше опорного
            i += 1  # Переходим к следующему элементу

        j -= 1  # Переходим к предыдущему элементу
        while nums[j] > pivot:  # Пока элемент больше опорного
            j -= 1  # Переходим к предыдущему элементу

        if i >= j:  # Если индексы встретились
            return j  # Возвращаем индекс разделения

        nums[i], nums[j] = nums[j], nums[i]  # Меняем местами элементы

def quick_sort(nums):
    """Сортировка списка методом быстрой сортировки."""
    def _quick_sort(items, low, high):  # Внутренняя функция для рекурсивной сортировки
        if low < high:  # Если длина списка больше 1
            split_index = partition(items, low, high)  # Разделяем список на две части
            _quick_sort(items, low, split_index)  # Рекурсивно сортируем левую часть
            _quick_sort(items, split_index + 1, high)  # Рекурсивно сортируем правую часть

    _quick_sort(nums, 0, len(nums) - 1)  # Вызываем внутреннюю функцию для всего списка

plot_performance(data_sizes, bubble_sort, selection_sort, insertion_sort, heap_sort, merge_sort, quick_sort)  # Строим график производительности
