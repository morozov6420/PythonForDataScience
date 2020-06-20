# clear all variables
# for name in dir():
#     if not name.startswith('_'):
#         del globals()[name]

import numpy as np
# Создание массива из int
np.random.seed(42)
x = np.random.randint(5, size = (5,5)) # массив 5 на 5 с элементами от 0 до 4
# Сохранение массива в файл
np.savetxt('day2_19.06/homework/matrix.csv', x, fmt = '%i', delimiter = ',')
# Чтение массива из файла
matrix = np.loadtxt('day2_19.06/homework/matrix.csv', delimiter = ',')
# Смотрим, какие элементы максимальные и минимальные
max_id = matrix == matrix.max()
min_id = matrix == matrix.min()
# Меняем элементы местами
print("До замены:\n", matrix)
matrix[max_id], matrix[min_id] = matrix.min(), matrix.max()
print("После замены:\n", matrix)