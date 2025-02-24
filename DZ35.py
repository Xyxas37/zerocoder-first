import pandas as pd

data = {
    'Набор А': [80, 90, 100, 110, 135],
    'Набор B': [80, 95, 100, 105, 145],

}
df = pd.DataFrame(data)

stdA = df['Набор А'].std()
stdB = df['Набор B'].std()

print(f"стандартное отклонение 1 набор - {stdA}")
print(f"стандартное отклонение 2 набор - {stdB}")
