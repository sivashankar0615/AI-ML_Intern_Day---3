# -*- coding: utf-8 -*-
"""intern_day_3_code.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Hck4K0NmuXE26MYyF7VeVtSSdZku2pUt
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error,mean_squared_error,r2_score

data=pd.read_csv('/content/Housing.csv')
print(data.head())


print(data.isnull().sum())

df = data.dropna()

x=df[['area','bedrooms']]
y=df['price']

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.3,random_state=42)

model=LinearRegression()
model.fit(x_train,y_train)

y_pred = model.predict(x_test)

mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f'Mean Absolute Error (MAE): {mae}')
print(f'Mean Squared Error (MSE): {mse}')
print(f'R-squared (R²): {r2}')

X_area = df[['area']]
y_price = df['price']

X_train_area, X_test_area, y_train_price, y_test_price = train_test_split(X_area, y_price, test_size=0.2, random_state=42)

model_area = LinearRegression()
model_area.fit(X_train_area, y_train_price)

y_pred_area = model_area.predict(X_test_area)

plt.scatter(X_test_area, y_test_price, color='blue', label='Actual')
plt.plot(X_test_area, y_pred_area, color='red', linewidth=2, label='Predicted Line')
plt.xlabel('Area')
plt.ylabel('Price')
plt.title('Area vs Price Linear Regression')
plt.legend()
plt.show()

X_area = df[['bedrooms']]
y_price = df['price']

X_train_area, X_test_area, y_train_price, y_test_price = train_test_split(X_area, y_price, test_size=0.2, random_state=42)

model_area = LinearRegression()
model_area.fit(X_train_area, y_train_price)

y_pred_area = model_area.predict(X_test_area)

# Plotting
plt.scatter(X_test_area, y_test_price, color='blue', label='Actual')
plt.plot(X_test_area, y_pred_area, color='red', linewidth=2, label='Predicted Line')
plt.xlabel('Bedrooms')
plt.ylabel('Price')
plt.title('Bedrooms vs Price Linear Regression')
plt.legend()
plt.show()