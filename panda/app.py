import pandas as pd

df = pd.DataFrame(
    {
        'points': [25, 12, 15, 14, 19],
        'assists': [5, 7, 7, 9, 12],
        'rebounds': [11, 8, 10, 6, 6],
        'bonus': [21, 10, 9, 8, 7]

    }
)
# print(df)
# print(df.describe())
# print(df.std())
# print(df.mean())
# print(df.count())
# print(df.points.mean())
print((df-df.min())/(df.max() - df.min()))