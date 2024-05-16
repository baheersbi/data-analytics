import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df = pd.DataFrame({
    'team': np.repeat(['A', 'B', 'C'], 100),
    'points': np.random.normal(loc=20, scale=2, size=300)
})


num_bins = 4
df['points_bin'] = pd.qcut(df['points'], q=num_bins, labels=False)


print(df.head())
print(df.tail())
print(df['points_bin'].value_counts())


df['points_bin'].value_counts().sort_index().plot(kind='bar')
plt.xlabel('Bin')
plt.ylabel('Frequency')
plt.title('Equal Frequency Binning of Points')
plt.show()
