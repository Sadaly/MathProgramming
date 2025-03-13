import numpy as np
import matplotlib.pyplot as plt


# Проверка, можно ли выиграть за один ход
def can_win_in_one_move(field, player):
    directions = [(0, 1), (1, 0), (1, 1), (1, -1)]  # горизонт, вертикаль, диагонали
    m, n = len(field), len(field[0])  # Размеры поля

    for i in range(m):
        for j in range(n):
            if field[i][j] == player:
                for dx, dy in directions:
                    player_count = 1  # Счётчик для символов игрока
                    empty_count = 0  # Счётчик пустых клеток
                    # Проверяем в обе стороны
                    for step in range(1, 5):
                        ni, nj = i + dx * step, j + dy * step
                        if 0 <= ni < m and 0 <= nj < n:
                            if field[ni][nj] == player:
                                player_count += 1
                            elif field[ni][nj] == '.':
                                empty_count += 1
                            else:
                                break
                        else:
                            break

                    # Если у нас есть ровно 5 ячеек и только одно пустое место,
                    # то можно выиграть за один ход
                    if player_count + empty_count == 5 and empty_count == 1:
                        return True

    return False


# Визуализация поля
def plot_board(field):
    m, n = len(field), len(field[0])  # Размеры поля
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.set_xticks(np.arange(n + 1) - 0.5, minor=True)
    ax.set_yticks(np.arange(m + 1) - 0.5, minor=True)
    ax.grid(which='minor', color='black', linestyle='-', linewidth=2)

    for i in range(m):
        for j in range(n):
            ax.text(j, i, field[i][j], ha='center', va='center', fontsize=20)

    ax.set_xticks([])
    ax.set_yticks([])
    plt.gca().invert_yaxis()
    plt.show()


# Пример использования:
# Определяем поле
field = [
    ['X', 'X', '.', 'O', 'O', 'X'],
    ['O', 'O', '.', 'X', 'O', '.'],
    ['X', 'O', 'X', '.', 'O', 'X'],
    ['.', 'X', 'O', 'X', '.', 'O'],
    ['X', 'X', 'X', '.', '.', 'O'],
    ['O', 'O', '.', '.', 'X', '.']
]

# Размеры поля
m, n = len(field), len(field[0])

# Проверка предвыигрышной ситуации
player = 'X'  # Проверяем для 'X'
if can_win_in_one_move(field, player):
    print(f"Игрок {player} может выиграть за один ход!")
else:
    print(f"Игрок {player} не может выиграть за один ход.")

# Визуализация поля
plot_board(field)
