import networkx as nx
import matplotlib.pyplot as plt

def draw_graph(G, pos, title, edge_labels=None):
    """Функция для отрисовки графа."""
    plt.figure(figsize=(8, 6))
    nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray', node_size=1500, font_size=12)
    if edge_labels:
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=12)
    plt.title(title)
    plt.show()

# 1. Граф для нахождения кратчайшего пути
dijkstra_graph = nx.DiGraph()
dijkstra_edges = [(0, 1, 4), (0, 2, 3), (1, 2, 1), (1, 3, 2), (2, 3, 4)]
dijkstra_graph.add_weighted_edges_from(dijkstra_edges)
pos = nx.spring_layout(dijkstra_graph)

draw_graph(dijkstra_graph, pos, "Граф для поиска кратчайшего пути", edge_labels={(u, v): w for u, v, w in dijkstra_edges})
shortest_path = nx.dijkstra_path(dijkstra_graph, source=0, target=3, weight='weight')
print("Кратчайший путь (Dijkstra) из 0 в 3:", shortest_path)

# 2. Граф для нахождения максимального потока
flow_graph = nx.DiGraph()
flow_edges = [(0, 1, 16), (0, 2, 13), (1, 2, 10), (1, 3, 12), (2, 1, 4), (2, 4, 14), (3, 2, 9), (3, 5, 20), (4, 3, 7), (4, 5, 4)]
for u, v, capacity in flow_edges:
    flow_graph.add_edge(u, v, capacity=capacity)
pos = nx.spring_layout(flow_graph)

draw_graph(flow_graph, pos, "Граф для нахождения максимального потока", edge_labels={(u, v): w for u, v, w in flow_edges})
max_flow = nx.maximum_flow(flow_graph, 0, 5)
print("Максимальный поток из 0 в 5:", max_flow[0])

# Функция для отрисовки графа
def draw_graph(G, pos, title, edge_labels=None):
    plt.figure(figsize=(8, 6))
    nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray', node_size=1500, font_size=12)
    if edge_labels:
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=12)
    plt.title(title)
    plt.show()

# 3. Граф для нахождения потока минимальной стоимости
min_cost_graph = nx.DiGraph()

# Добавляем рёбра с пропускной способностью и стоимостью
min_cost_edges = [(0, 1, 5, 6), (0, 2, 5, 6), (1, 2, 15, 1), (1, 3, 10, 3), (2, 3, 10, 1)]
for u, v, cap, cost in min_cost_edges:
    min_cost_graph.add_edge(u, v, capacity=cap, weight=cost)

# Задаём спрос для узлов
min_cost_graph.add_node(0, demand=-5)  # Источник
min_cost_graph.add_node(3, demand=5)   # Сток

# Отображаем граф
pos = nx.spring_layout(min_cost_graph)
draw_graph(min_cost_graph, pos, "Граф для потока минимальной стоимости", edge_labels={(u, v): f'{d["weight"]}' for u, v, d in min_cost_graph.edges(data=True)})

# Используем функцию для нахождения минимального потока
flow_dict = nx.min_cost_flow(min_cost_graph)

# Считаем стоимость минимального потока
min_cost = nx.min_cost_flow_cost(min_cost_graph)

# Выводим результат
print("Стоимость минимального потока:", min_cost)

# Также выводим сам поток, чтобы понять, что происходит
print("Поток по рёбрам:", flow_dict)