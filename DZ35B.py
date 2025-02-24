import pandas as pd
import numpy as np


dates = pd.date_range(start='2025-01-20', periods=30, freq='D')
values = np.random.rand(30)
df = pd.DataFrame({'Date': dates, 'Value': values})
df.set_index('Date', inplace=True)

print(df)

month = df.resample('M').mean()


print(month)