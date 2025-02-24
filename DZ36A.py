import numpy as np
import matplotlib.pyplot as plt

# Параметры нормального распределения
mean = 0       # Среднее значение
std_dev = 1    # Стандартное отклонение
num_samples = 1000  # Количество значений

# Генерация случайных чисел с нормальным распределением
data = np.random.normal(mean, std_dev, num_samples)

# Построение гистограммы
plt.hist(data, bins=30, color='skyblue', edgecolor='black', alpha=0.7)
plt.xlabel("Значение")
plt.ylabel("Частота")
plt.title("Гистограмма нормального распределения")
plt.grid(True)

# Показать график
plt.show()
