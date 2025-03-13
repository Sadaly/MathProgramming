from scipy.optimize import minimize_scalar


# Целевая функция L(x) = x1 + 2x2 - x3
def objective(lambda_val):
    # Выражаем x1, x2, x3 через lambda
    x1 = 1 - 2 * lambda_val
    x2 = 1 + lambda_val
    x3 = 0  # x3 = 0 для максимизации L(x)

    # Проверяем ограничения x1, x2, x3 >= 0
    if x1 < 0 or x2 < 0 or x3 < 0:
        return -float('inf')  # Возвращаем -бесконечность, если ограничения нарушены

    # Вычисляем значение целевой функции
    return x1 + 2 * x2 - x3


# Находим оптимальное значение lambda
result = minimize_scalar(lambda l: -objective(l), bounds=(-1, 0.5), method='bounded')

# Проверяем успешность оптимизации
if result.success:
    optimal_lambda = result.x
    max_L = -result.fun  # Минус, так как мы минимизировали -L(x)

    # Вычисляем оптимальные x1, x2, x3
    x1 = 1 - 2 * optimal_lambda
    x2 = 1 + optimal_lambda
    x3 = 0

    # Вывод результатов
    print(f"Оптимальное значение λ: {optimal_lambda}")
    print(f"Максимальное значение L(x): {max_L}")
    print(f"Оптимальные значения x1, x2, x3: {x1}, {x2}, {x3}")
else:
    print("Оптимизация не удалась.")