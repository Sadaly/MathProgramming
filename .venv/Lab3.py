import numpy as np
from scipy.optimize import linprog

# Коэффициенты целевой функции для максимизации
c = np.array([1, 4, 6, 3])  # Для максимизации: x1 - 4x2 + 6x3 + 3x4 => -x1 + 4x2 - 6x3 - 3x4

# Ограничения (преобразуем их в форму ≤)
A = np.array([[-3, -2, -1, -1],     # 3x1 + 2x2 + x3 + x4 ≤ 6
              [-1, -7, 5, 3]])  # x1 + 7x2 - 5x3 - 3x4 ≤ 4

# Правая часть ограничений
b = np.array([-6, -4])

# Неотрицательные переменные (x1, x2, x3, x4 ≥ 0)
bounds = [(0, None)] * 4  # Для всех переменных x1, x2, x3, x4 >= 0

# Решаем задачу методом симплекс
result = linprog(c, A_ub=A, b_ub=b, bounds=bounds, method='simplex')

# Проверка результата
if result.success:
    print("Оптимальное решение:")
    print(f"x1 = {result.x[0]}")
    print(f"x2 = {result.x[1]}")
    print(f"x3 = {result.x[2]}")
    print(f"x4 = {result.x[3]}")
    print(f"Значение целевой функции = {result.fun}")  # Для минимизации
else:
    print("Нет решения.")
    print("Диагностика проблемы:")
    print("Сообщение ошибки: ", result.message)
    print("Код ошибки: ", result.status)
