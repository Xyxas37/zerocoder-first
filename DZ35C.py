import pandas as pd
import matplotlib.pyplot as plt

data = {'Value': [1, 2, 2, 3, 3, 3, 4, 4, 4, 5, 6, 7, 8, 9, 10, 55]}
df = pd.DataFrame(data)


#df['Value'].hist()
#plt.show()

df.boxplot(column='Value')
plt.show()

Q1 = df['Value'].quantile(0.25)
Q3 = df['Value'].quantile(0.75)

IQR = Q3 - Q1

downside = Q1 - 1.5 * IQR
upside = Q3 + 1.5 * IQR

df_new = df[(df['Value'] >= downside) & (df['Value'] <= upside)]
df_new.boxplot(column='Value')
plt.show()