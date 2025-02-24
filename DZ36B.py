import numpy as np
import matplotlib.pyplot as plt

# Генерация случайных данных
num_points = 100  # Количество точек
x = np.random.rand(num_points)  # X-координаты (от 0 до 1)
y = np.random.rand(num_points)  # Y-координаты (от 0 до 1)

# Построение диаграммы рассеяния
plt.scatter(x, y, color='red', alpha=0.6, edgecolors='black')
plt.xlabel("X-значения")
plt.ylabel("Y-значения")
plt.title("Диаграмма рассеяния случайных данных")
plt.grid(True)

# Показать график
plt.show()
