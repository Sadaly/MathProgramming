# Параметры задачи
num_vehicles = 20  # Количество автомобилей
cost_repair = 75  # Стоимость профилактического ремонта одного автомобиля
cost_breakdown = 200  # Стоимость случайной поломки одного автомобиля


# Вероятности поломки для каждого месяца
def get_probability(m):
    if m == 1:
        return 0
    elif 2 <= m <= 10:
        return 0.02 + 0.01 * (m - 1)
    else:
        return 0.13


# Рассчитываем ожидаемые затраты для каждого периода
def calculate_costs(max_period):
    results = []
    for T in range(1, max_period + 1):
        # Сумма вероятностей поломки за период T
        total_probability = sum(get_probability(m) for m in range(1, T + 1))

        # Затраты на случайные поломки
        breakdown_cost = num_vehicles * cost_breakdown * total_probability

        # Затраты на профилактический ремонт
        repair_cost = num_vehicles * cost_repair

        # Общие затраты
        total_cost = repair_cost + breakdown_cost

        results.append((T, total_cost))
    return results


# Находим оптимальный период
def find_optimal_period(results):
    optimal_period = min(results, key=lambda x: x[1])
    return optimal_period


# Основная программа
max_period = 12  # Максимальный период для анализа
results = calculate_costs(max_period)
optimal_period, min_cost = find_optimal_period(results)

# Вывод результатов
print("Период (месяцы) | Ожидаемые затраты (долл.)")
print("----------------|--------------------------")
for period, cost in results:
    print(f"{period:^15} | {cost:^25}")

print(f"\nОптимальный период: {optimal_period} месяцев")
print(f"Минимальные ожидаемые затраты: {min_cost} долл.")