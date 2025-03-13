from scipy.optimize import minimize


def maximize_z(n, c):
    # Функция для минимизации (минимизируем -z, чтобы максимизировать z)
    def objective(y):
        return -sum(yi ** 2 for yi in y)

    # Ограничение: произведение y_i равно c
    def constraint(y):
        product = 1
        for yi in y:
            product *= yi
        return product - c

    # Начальное предположение: все y_i равны (c^(1/n))
    y0 = [c ** (1 / n)] * n

    # Ограничения
    cons = {'type': 'eq', 'fun': constraint}

    # Границы: y_i >= 0
    bounds = [(0, None) for _ in range(n)]

    # Решение задачи оптимизации
    result = minimize(objective, y0, method='SLSQP', bounds=bounds, constraints=cons)

    if result.success:
        # Возвращаем максимальное значение z и значения y
        return -result.fun, result.x
    else:
        raise ValueError("Оптимизация не удалась")


# Пример использования
n = 3
c = 8
max_z, y_values = maximize_z(n, c)
print(f"Максимальное значение z: {max_z}")
print(f"Оптимальные значения y: {y_values}")