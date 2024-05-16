import pandas as pd
from sklearn import linear_model

# Original data with index_price provided
data = {
    'year': [2017, 2017, 2017, 2017, 2017, 2017, 2017, 2017, 2017, 2017, 2016, 2016, 2016, 2016, 2016, 2016, 2016, 2016, 2016, 2016],
    'month': [12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 12, 11, 10, 9, 8, 7, 6, 5],
    'interest_rate': [2.75, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.25, 2.25, 2.25, 2, 2, 2, 2, 2, 1.75, 1.75, 1.75, 1.75],
    'unemployment_rate': [5.3, 5.3, 5.3, 5.3, 5.3, 5.4, 5.6, 5.5, 5.5, 5.5, 5.6, 5.7, 5.9, 6, 5.9, 5.8, 6.1, 6.2, 6.1, 5.9],
    'index_price': [1464, 1394, 1357, 1293, 1256, 1254, 1234, 1195, 1159, 1167, 1130, 1075, 1047, 965, 943, 958, 971, 949, 884, 866]
}

df = pd.DataFrame(data)

x_train = df[['interest_rate', 'unemployment_rate']]
y_train = df['index_price']

regr = linear_model.LinearRegression()
regr.fit(x_train, y_train)

new_data = {
    'year': [2018, 2018, 2018, 2018],
    'month': [1, 2, 3, 4],
    'interest_rate': [1.75, 1.75, 1.75, 1.75],
    'unemployment_rate': [6.1, 6.1, 6.1, 6.1]
}

df_new = pd.DataFrame(new_data)

x_new = df_new[['interest_rate', 'unemployment_rate']]
predicted_index_price = regr.predict(x_new)

df_new['predicted_index_price'] = predicted_index_price

print("New data with predicted index_price:")
print(df_new)
