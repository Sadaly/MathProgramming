import numpy as np
import heapq
import networkx as nx
import matplotlib.pyplot as plt
from scipy.optimize import linprog

# Исходный граф (ребра: вершина1, вершина2, вес)
test_edges = [(0, 1, 4), (0, 2, 3), (1, 2, 1), (1, 3, 2), (2, 3, 4), (2, 4, 4)]

# Автоматическое определение количества вершин
num_nodes = max(max(u, v) for u, v, _ in test_edges) + 1


def prim_mst(edges, n):
    """Алгоритм Прима для поиска минимального остовного дерева (MST)."""
    graph = {i: [] for i in range(n)}
    for u, v, w in edges:
        graph[u].append((w, v))
        graph[v].append((w, u))

    mst, visited, heap = [], set(), [(0, 0, -1)]
    while heap and len(visited) < n:
        w, u, prev = heapq.heappop(heap)
        if u in visited:
            continue
        visited.add(u)
        if prev != -1:
            mst.append((prev, u, w))
        for next_w, v in graph[u]:
            if v not in visited:
                heapq.heappush(heap, (next_w, v, u))
    return mst


def dijkstra(graph, start):
    """Алгоритм Дейкстры для поиска кратчайшего пути."""
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    pq = [(0, start)]
    paths = {node: [] for node in graph}
    paths[start] = [start]

    while pq:
        current_distance, current_node = heapq.heappop(pq)
        if current_distance > distances[current_node]:
            continue
        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
                paths[neighbor] = paths[current_node] + [neighbor]
    return distances, paths


def draw_graph(edges, mst_edges=None, dijkstra_paths=None):
    """Функция для отрисовки графа, MST и кратчайших путей."""
    G = nx.Graph()
    for u, v, w in edges:
        G.add_edge(u, v, weight=w)

    pos = nx.spring_layout(G)
    plt.figure(figsize=(8, 6))
    labels = {(u, v): w for u, v, w in edges}
    nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray', node_size=1500, font_size=12)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, font_size=12)

    # Отрисовка MST
    if mst_edges:
        mst_G = nx.Graph()
        for u, v, w in mst_edges:
            mst_G.add_edge(u, v, weight=w)
        nx.draw(mst_G, pos, edge_color='red', width=2, node_color='lightblue', with_labels=True)

    # Отрисовка кратчайшего пути (например, до вершины 3)
    if dijkstra_paths and 3 in dijkstra_paths:
        path_edges = [(dijkstra_paths[3][i], dijkstra_paths[3][i + 1]) for i in range(len(dijkstra_paths[3]) - 1)]
        path_G = nx.Graph()
        path_G.add_edges_from(path_edges)
        nx.draw(path_G, pos, edge_color='blue', width=2.5, node_color='lightblue', with_labels=True)

    plt.title("Граф с MST (красный) и кратчайшим путем (синий)")
    plt.show()


# Создание графа для Dijkstra
graph = {i: [] for i in range(num_nodes)}
for u, v, w in test_edges:
    graph[u].append((v, w))
    graph[v].append((u, w))

# Запускаем алгоритмы
mst_result = prim_mst(test_edges, num_nodes)
dijkstra_result, dijkstra_paths = dijkstra(graph, 0)

# Визуализация графа с MST и кратчайшим путем
draw_graph(test_edges, mst_edges=mst_result, dijkstra_paths=dijkstra_paths)