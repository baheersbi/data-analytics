import pandas as pd

df = pd.read_csv('data.csv')

# df['Date'] = pd.to_datetime(df['Date'])

# print(df.Pulse.mean())
print(df.to_string())

# df = pd.DataFrame(
#     {
#         'points': [25, 12, 15, 14, 19],
#         'assists': [5, 7, 7, 9, 12],
#         'rebounds': [11, 8, 10, 6, 6],
#         'bonus': [45, 34, 8, 9, 0]
#
#      }
# )
# print(df.describe())
# print(df.points.describe())
# print(df.points.std())
# print(df.min())
# print(df.mean())
# print(df.head(4).mean())
# print(df.head(1).mean())
# print(df.assists.min())