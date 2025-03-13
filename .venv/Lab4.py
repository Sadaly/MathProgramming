import numpy as np

# Исходные данные
supply = [900, 100, 100, 600, 400]  # Запасы поставщиков
demand = [500, 300, 400, 500, 400]  # Потребности потребителей
costs = np.array([
    [5, 4, 7, 2, 4],  # Стоимости от A1
    [7, 4, 2, 1, 5],  # Стоимости от A2
    [4, 3, 2, 7, 8],  # Стоимости от A3
    [5, 4, 7, 1, 3],  # Стоимости от A4
    [4, 5, 6, 2, 4]  # Стоимости от A5
])


# Метод северо-западного угла
def northwest_corner(supply, demand, costs):
    supply_copy = supply.copy()
    demand_copy = demand.copy()
    allocation = np.zeros_like(costs)
    i, j = 0, 0
    while i < len(supply_copy) and j < len(demand_copy):
        quantity = min(supply_copy[i], demand_copy[j])
        allocation[i, j] = quantity
        supply_copy[i] -= quantity
        demand_copy[j] -= quantity
        if supply_copy[i] == 0:
            i += 1
        if demand_copy[j] == 0:
            j += 1

    # Проверяем, все ли потребности удовлетворены
    if np.sum(allocation, axis=0).tolist() != demand:
        # Если нет, продолжаем распределение
        for j in range(len(demand_copy)):
            if demand_copy[j] > 0:
                for i in range(len(supply_copy)):
                    if supply_copy[i] > 0:
                        quantity = min(supply_copy[i], demand_copy[j])
                        allocation[i, j] += quantity
                        supply_copy[i] -= quantity
                        demand_copy[j] -= quantity
                        if demand_copy[j] == 0:
                            break

    total_cost = np.sum(allocation * costs)
    return allocation, total_cost


# Метод наименьшей стоимости
def least_cost(supply, demand, costs):
    supply_copy = supply.copy()
    demand_copy = demand.copy()
    allocation = np.zeros_like(costs)
    while True:
        # Находим клетку с минимальной стоимостью
        min_cost = np.inf
        min_i, min_j = -1, -1
        for i in range(len(supply_copy)):
            for j in range(len(demand_copy)):
                if supply_copy[i] > 0 and demand_copy[j] > 0 and costs[i, j] < min_cost:
                    min_cost = costs[i, j]
                    min_i, min_j = i, j
        if min_i == -1:
            break
        quantity = min(supply_copy[min_i], demand_copy[min_j])
        allocation[min_i, min_j] = quantity
        supply_copy[min_i] -= quantity
        demand_copy[min_j] -= quantity
    total_cost = np.sum(allocation * costs)
    return allocation, total_cost


# Метод Фогеля
def vogel_approximation(supply, demand, costs):
    supply_copy = supply.copy()
    demand_copy = demand.copy()
    allocation = np.zeros_like(costs)

    while True:
        # Вычисляем разницы для строк
        row_diff = []
        for i in range(len(supply_copy)):
            if supply_copy[i] > 0:
                row = [costs[i, j] for j in range(len(demand_copy)) if demand_copy[j] > 0]
                if len(row) >= 2:
                    row.sort()
                    row_diff.append(row[1] - row[0])
                else:
                    row_diff.append(0)
            else:
                row_diff.append(-1)  # Игнорируем строки с нулевым запасом

        # Вычисляем разницы для столбцов
        col_diff = []
        for j in range(len(demand_copy)):
            if demand_copy[j] > 0:
                col = [costs[i, j] for i in range(len(supply_copy)) if supply_copy[i] > 0]
                if len(col) >= 2:
                    col.sort()
                    col_diff.append(col[1] - col[0])
                else:
                    col_diff.append(0)
            else:
                col_diff.append(-1)  # Игнорируем столбцы с нулевой потребностью

        # Проверяем, остались ли ненулевые запасы и потребности
        if max(row_diff) == -1 and max(col_diff) == -1:
            break

        # Находим максимальную разницу
        max_row_diff = max(row_diff)
        max_col_diff = max(col_diff)

        if max_row_diff >= max_col_diff:
            i = row_diff.index(max_row_diff)
            # Находим минимальную стоимость в строке i
            min_cost = np.inf
            min_j = -1
            for j in range(len(demand_copy)):
                if demand_copy[j] > 0 and costs[i, j] < min_cost:
                    min_cost = costs[i, j]
                    min_j = j
            j = min_j
        else:
            j = col_diff.index(max_col_diff)
            # Находим минимальную стоимость в столбце j
            min_cost = np.inf
            min_i = -1
            for i in range(len(supply_copy)):
                if supply_copy[i] > 0 and costs[i, j] < min_cost:
                    min_cost = costs[i, j]
                    min_i = i
            i = min_i

        # Распределяем груз
        quantity = min(supply_copy[i], demand_copy[j])
        allocation[i, j] = quantity
        supply_copy[i] -= quantity
        demand_copy[j] -= quantity

    total_cost = np.sum(allocation * costs)
    return allocation, total_cost


# Решение задачи
print("Метод северо-западного угла:")
allocation_nw, cost_nw = northwest_corner(supply, demand, costs)
print("Распределение:")
print(allocation_nw)
print(f"Общая стоимость: {cost_nw}\n")

print("Метод наименьшей стоимости:")
allocation_lc, cost_lc = least_cost(supply, demand, costs)
print("Распределение:")
print(allocation_lc)
print(f"Общая стоимость: {cost_lc}\n")

print("Метод Фогеля:")
allocation_vogel, cost_vogel = vogel_approximation(supply, demand, costs)
print("Распределение:")
print(allocation_vogel)
print(f"Общая стоимость: {cost_vogel}\n")

