# -*- coding: utf-8 -*-
"""ISB_Proyecto_Final.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/17S3rwi6t--ydaLuMRSSyxuFtRmkR7Tdl
"""

!pip install scikit-learn

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
from sklearn.preprocessing import StandardScaler

data = pd.read_csv('caracteristicas_entrenamiento_final2.csv')
print(data.head())

# Separar las características (X) y la variable objetivo (y)
X = data.drop('Promedio', axis=1)
y = data['Promedio']

# Dividir el conjunto de datos en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Inicializar y entrenar el modelo de regresión lineal en las características polinómicas
model = LinearRegression()
model.fit(X_train_scaled, y_train)

# Realizar predicciones en el conjunto de prueba
y_pred = model.predict(X_test_scaled)

# Evaluar el rendimiento del modelo
mse = mean_squared_error(y_test, y_pred)
print(f'Mean Squared Error: {mse}')
r2 = r2_score(y_test, y_pred)
print(f'R² Score: {r2}')
mae = mean_absolute_error(y_test, y_pred)
print(f'Mean Absolute Error (MAE): {mae}')

nuevas_caracteristicas = pd.read_excel('caracteristicas_bitalino.xlsx')
print(nuevas_caracteristicas.head())

nueva_prediccion = model.predict(nuevas_caracteristicas)
print(f'Predicción de presión arterial: {nueva_prediccion}')

poly = PolynomialFeatures(degree=9)
X_train_poly = poly.fit_transform(X_train_scaled)
X_test_poly = poly.transform(X_test_scaled)
# Inicializar y entrenar el modelo de regresión lineal en las características polinómicas
model2 = LinearRegression()
model2.fit(X_train_poly, y_train)

# Realizar predicciones en el conjunto de prueba
y_pred = model2.predict(X_test_poly)

# Evaluar el rendimiento del modelo
mse = mean_squared_error(y_test, y_pred)
print(f'Mean Squared Error: {mse}')
r2 = r2_score(y_test, y_pred)
print(f'R² Score: {r2}')
mae = mean_absolute_error(y_test, y_pred)
print(f'Mean Absolute Error (MAE): {mae}')

nuevas_caracteristicas_poly = poly.fit_transform(nuevas_caracteristicas)
nueva_prediccion = model2.predict(nuevas_caracteristicas_poly)
print(f'Predicción de presión arterial: {nueva_prediccion}')