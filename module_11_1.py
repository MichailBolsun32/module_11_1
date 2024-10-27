import pandas
#Библиотека pandas для обработка данных из разнообразных источников:

# Поддержка различных форматов файлов: CSV, Excel, SQL, JSON и других.
# Возможность работы с данными из веб-источников.
# Индексация и фильтрация:
# Оптимизация работы с большими объемами данных


data = pandas.read_excel('test_data.xlsx') # считал файл .xlsx в data

# print(data.head()) # выводит первых 5 строк для ознакомления
print(data.tail(n=6)) # выводит нужное количество строк

#print(data.info()) # Информация о данных:
#print(data.describe()) #Описание числовых данных столбцов
#print(data['Product name']) # Получение данных из столбца 'column_name'

# Получение данных по индексу (например, 0-й индекс)
print("Получение данных по индексу (например, 0-й индекс)")
first_row = data.iloc[0]
print(first_row)
# Получение данных из первой строки и первого столбца
print('Получение данных из первой строки и первого столбца')
value = data.iloc[0, 0]
print(value)

column_sum = data['sales'].sum() # подсчет суммы в столбце
print(f'К-во проданных товаров за день-{column_sum}')
column_min = data['sales'].min() # определение min значения в столбце
print(f'Минимальное к-во проданного товара за день-{column_min}')
column_mean = data['sales'].mean().astype(int) # определение среднего значения в столбце и округлить до целого
print(f'Среднее к-во проданных товарав за день-{column_mean}')
print()

#Для работы с массивами используют библиотеку numpy
import numpy
# Создание массива чисел
array = numpy.array([1, 2, 3, 4, 5])

# Выполнение математических операций
sum_array = numpy.sum(array)  # Сумма элементов
mean_array = numpy.mean(array)  # Среднее значение
std_array = numpy.std(array)  # Стандартное отклонение, одно из базовых велечин в статистике
squared_array = array ** 2  # Квадраты элементов

# Вывод результатов в консоль
print("Исходный массив:", array)
print("Сумма элементов:", sum_array)
print("Среднее значение:", mean_array)
print("Стандартное отклонение:", std_array)
print("Квадраты элементов:", squared_array)

# Matplotlib - мощный инструментом для визуализации и анализа данных.

import matplotlib.pyplot as plt

# Создание данных
x = numpy.linspace(0, 10, 100)# arrey со 100 равномерными точками от 0 до 10
y = numpy.sin(x)# arrey c резельтатом вычисления ф-ции sin от x

# Создание графика
plt.plot(x, y, label='sin(x)', color='blue')

# Настройка графика
plt.title('График функции sin(x)')
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.legend() #легенда

# Показ графика
plt.grid() # сетка
plt.show() # график

