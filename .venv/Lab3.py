import numpy as np
import tkinter as tk
from tkinter import messagebox
from scipy.optimize import linprog


def solve_lp():
    try:
        # Получаем коэффициенты целевой функции
        c = [-float(entry_obj.get()) for entry_obj in c_entries]

        # Получаем коэффициенты ограничений
        A = []
        for row in A_entries:
            A.append([-float(entry.get()) for entry in row])

        # Получаем правую часть ограничений
        b = [-float(entry.get()) for entry in b_entries]

        # Решаем задачу линейного программирования
        result = linprog(c, A_ub=A, b_ub=b, bounds=[(0, None)] * len(c), method='simplex')

        # Выводим результаты
        if result.success:
            solution_text.set(f"Оптимальное решение:\n" + "\n".join([f"x{i + 1} = {result.x[i]:.4f}" for i in range(
                len(result.x))]) + f"\n\nЗначение целевой функции: {-result.fun:.4f}")
        else:
            solution_text.set(f"Нет решения. Ошибка: {result.message}")
    except Exception as e:
        messagebox.showerror("Ошибка", f"Некорректные данные: {e}")


# Создаем основное окно
root = tk.Tk()
root.title("Линейное программирование")

tk.Label(root, text="Введите коэффициенты целевой функции:").grid(row=0, column=0, columnspan=4)
c_entries = [tk.Entry(root, width=5) for _ in range(4)]
for i, entry in enumerate(c_entries):
    entry.grid(row=1, column=i)

tk.Label(root, text="Введите коэффициенты ограничений:").grid(row=2, column=0, columnspan=4)
A_entries = [[tk.Entry(root, width=5) for _ in range(4)] for _ in range(2)]
for i, row in enumerate(A_entries):
    for j, entry in enumerate(row):
        entry.grid(row=3 + i, column=j)

tk.Label(root, text="Введите правую часть ограничений:").grid(row=5, column=0, columnspan=4)
b_entries = [tk.Entry(root, width=5) for _ in range(2)]
for i, entry in enumerate(b_entries):
    entry.grid(row=6, column=i)

solution_text = tk.StringVar()
tk.Label(root, textvariable=solution_text, justify=tk.LEFT).grid(row=8, column=0, columnspan=4)

tk.Button(root, text="Рассчитать", command=solve_lp).grid(row=7, column=0, columnspan=4)

root.mainloop()
