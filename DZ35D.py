import pandas as pd
import numpy as np

data = {
    "Имя": ["Алина", "Борис", "Виктор", "Галина", "Дмитрий", "Елена", "Женя", "Зоя", "Игорь", "Ксения"],
    "Математика": [5, 4, 3, 5, 2, 4, 5, 3, 4, 5],
    "Физика": [3, 5, 4, 4, 2, 3, 5, 5, 4, 4],
    "Химия": [4, 3, 5, 5, 3, 2, 4, 5, 4, 3],
    "Литература": [5, 4, 4, 3, 5, 4, 4, 3, 5, 4],
    "История": [4, 3, 3, 4, 3, 2, 2, 3, 3, 2]
}

df = pd.DataFrame(data)

print("Первые 5 строк DataFrame:")
print(df.head())


mean_scores = df.iloc[:, 1:].mean()
print("\nСредние оценки по предметам:")
print(mean_scores)

median_scores = df.iloc[:, 1:].median()
print("\nМедианные оценки по предметам:")
print(median_scores)

Q1_math = df['Математика'].quantile(0.25)
Q3_math = df['Математика'].quantile(0.75)
print(f"\nQ1 (25-й процентиль) по математике: {Q1_math}")
print(f"Q3 (75-й процентиль) по математике: {Q3_math}")

IQR_math = Q3_math - Q1_math
print(f"IQR (межквартильный размах) по математике: {IQR_math}")

std_dev = df.iloc[:, 1:].std()
print("\nСтандартное отклонение по предметам:")
print(std_dev)
