import networkx as nx
import matplotlib.pyplot as plt


# Заполнение данных из таблицы
def input_data():
    works = {
        (1, 2): {'norm_duration': 3, 'norm_cost': 6, 'rush_duration': 2, 'rush_cost': 11},
        (1, 3): {'norm_duration': 5, 'norm_cost': 8, 'rush_duration': 3, 'rush_cost': 12},
        (1, 4): {'norm_duration': 4, 'norm_cost': 7, 'rush_duration': 8, 'rush_cost': 9},
        (2, 5): {'norm_duration': 10, 'norm_cost': 25, 'rush_duration': 8, 'rush_cost': 30},
        (3, 5): {'norm_duration': 8, 'norm_cost': 20, 'rush_duration': 6, 'rush_cost': 24},
        (3, 6): {'norm_duration': 15, 'norm_cost': 26, 'rush_duration': 12, 'rush_cost': 30},
        (4, 6): {'norm_duration': 13, 'norm_cost': 24, 'rush_duration': 10, 'rush_cost': 30},
        (5, 7): {'norm_duration': 3, 'norm_cost': 15, 'rush_duration': 6, 'rush_cost': 25},
        (6, 7): {'norm_duration': 4, 'norm_cost': 10, 'rush_duration': 3, 'rush_cost': 15},
    }
    return works


# Построение графика
def build_graph(works, mode='norm'):
    G = nx.DiGraph()
    for (start, end), data in works.items():
        duration = data[f'{mode}_duration']
        cost = data[f'{mode}_cost']
        G.add_edge(start, end, duration=duration, cost=cost)
    return G


# Визуализация графика
def draw_graph(G):
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_size=2000, node_color='skyblue', font_size=15, width=2, edge_color='gray')
    labels = nx.get_edge_attributes(G, 'duration')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    plt.show()


# Расчет временных характеристик и критического пути
def calculate_critical_path(G):
    early_start = {node: 0 for node in G.nodes}
    for u in nx.topological_sort(G):
        for _, v, data in G.edges(u, data=True):
            if early_start[v] < early_start[u] + data['duration']:
                early_start[v] = early_start[u] + data['duration']

    last_node = list(G.nodes)[-1]
    late_start = {node: early_start[last_node] for node in G.nodes}
    for u in reversed(list(nx.topological_sort(G))):
        for _, v, data in G.edges(u, data=True):
            if late_start[u] > late_start[v] - data['duration']:
                late_start[u] = late_start[v] - data['duration']

    slack = {node: late_start[node] - early_start[node] for node in G.nodes}
    critical_path = [node for node, sl in slack.items() if sl == 0]
    return early_start, late_start, slack, critical_path


# Основная функция
def main():
    works = input_data()
    print("Выберите режим (norm/rush):")
    mode = input().strip()
    G = build_graph(works, mode)
    draw_graph(G)
    early_start, late_start, slack, critical_path = calculate_critical_path(G)
    print("Ранние начала:", early_start)
    print("Поздние начала:", late_start)
    print("Резервы времени:", slack)
    print("Критический путь:", critical_path)

    total_cost = sum(data[f'{mode}_cost'] for data in works.values())
    print("Общая стоимость работ:", total_cost)


if __name__ == "__main__":
    main()