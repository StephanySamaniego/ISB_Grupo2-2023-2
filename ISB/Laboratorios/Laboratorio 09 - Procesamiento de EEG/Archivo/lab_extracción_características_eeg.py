# -*- coding: utf-8 -*-
"""Lab_Extracción_Características_EEG.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1C8tTENQccVA94MevJTVD_XkxiNqQnTqe
"""

pip install biosignalsnotebooks

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import re
import pywt
from scipy import signal
from scipy.signal import firwin, lfilter, welch
import biosignalsnotebooks as bsnb

"""## Obtenemos las señales sin filtrar

"""

arrayeeg = np.genfromtxt("eegSignal.txt", delimiter="\t",skip_header = 3, missing_values= 0)
#Extraemos la columna de la señal y creamos sus respectivos vectores tiempos
signaleeg = arrayeeg[:, 5]
signaleeg_3000 = signaleeg[0:3000]
Fs_eeg = 1000
Ts_eeg = 1/Fs_eeg
n_eeg= len(signaleeg)
t_eeg = np.arange(0,n_eeg*Ts_eeg,Ts_eeg)
t_eeg_3000 = np.arange(0,3000*Ts_eeg,Ts_eeg)
t_eeg

"""## Ploteamos las señales sin filtrar



"""

plt.plot(t_eeg_3000, signaleeg_3000, label="señal")      # graficamos la señal
plt.grid(linestyle=":")
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud")
plt.legend(loc="upper right")
plt.title("Señal EEG Sujeto Masculino - Sin Filtrar")
plt.show()

"""## Aplicamos el filtrado con Wavelet




"""

niveles_eeg = 8
coeficientes_eeg = pywt.wavedec(signaleeg, 'sym3', level=niveles_eeg)
coeficientes_eeg[0] = 0 * coeficientes_eeg[0]
coeficientes_eeg[1] = 0 * coeficientes_eeg[1]
coeficientes_eeg[8] = 0 * coeficientes_eeg[8]

plt.figure(figsize=(10, 10))
plt.subplot(niveles_eeg + 2, 1, 1)
plt.plot(t_eeg,signaleeg)
plt.ylabel('Voltaje (mV)')
plt.xlabel('Tiempo (s)')
plt.title('Señal Original')

for i, detalle in enumerate(coeficientes_eeg[1:]):  # Empezar desde el segundo nivel
    plt.subplot(niveles_eeg + 2, 1, i + 2)
    plt.plot(detalle)
    plt.title(f'Detalle Nivel {i+1}')

plt.subplot(niveles_eeg + 2, 1, niveles_eeg + 2)
plt.plot(coeficientes_eeg[0])
plt.title(f'Aproximación ')
plt.tight_layout()
plt.show()

umbral = 0.022

coeficientes_umbral_eeg = [pywt.threshold(c, umbral, mode='soft') for c in coeficientes_eeg]


senal_filtrada_eeg = pywt.waverec(coeficientes_umbral_eeg, 'sym3')

plt.figure(figsize=(10, 8))


plt.subplot(2, 1, 2)
plt.plot(t_eeg, senal_filtrada_eeg)
plt.xlim(0,3)
plt.ylim(-400,400)
plt.title('Señal EEG Sujeto Masculino - Filtro Wavelet (sym3)')
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud")

plt.tight_layout()
plt.show()

#Time Windows for Welchs method - theta band

sr=1000
win = 4 * sr # 4 seconds time windows.

#FFT with time windows using scipy.signal.welch
axis_x_1, axis_y_1 = welch(senal_filtrada_eeg, sr, nperseg=win)


freq_low = 1  #lower limit for alpha band
freq_high = 4 #Upper limit for alpha band

Signal_1 = np.logical_and(axis_x_1 >= freq_low, axis_x_1 <= freq_high)


fig2 = plt.figure(figsize=(15,20))

plt.subplot(4, 1, 1); plt.plot(axis_x_1[Signal_1], axis_y_1[Signal_1], "r"); plt.xlabel("Frequency(Hz)"); plt.title("Banda theta");
plt.ylabel("Amplitud");

#Time Windows for Welchs method -  Delta band
sr=1000
win = 4 * sr # 4 seconds time windows.

#FFT with time windows using scipy.signal.welch
axis_x_1, axis_y_1 = welch(senal_filtrada_eeg, sr, nperseg=win)


freq_low = 4 #lower limit for alpha band
freq_high = 7 #Upper limit for alpha band

Signal_1 = np.logical_and(axis_x_1 >= freq_low, axis_x_1 <= freq_high)


fig2 = plt.figure(figsize=(15,20))

plt.subplot(4, 1, 1); plt.plot(axis_x_1[Signal_1], axis_y_1[Signal_1], "r"); plt.xlabel("Frequency(Hz)"); plt.title("Banda delta");
plt.ylabel("Amplitud");

#Time Windows for Welchs method -  Alpha band
sr=1000
win = 4 * sr # 4 seconds time windows.

#FFT with time windows using scipy.signal.welch
axis_x_1, axis_y_1 = welch(senal_filtrada_eeg, sr, nperseg=win)


freq_low = 8 #lower limit for alpha band
freq_high = 12 #Upper limit for alpha band

Signal_1 = np.logical_and(axis_x_1 >= freq_low, axis_x_1 <= freq_high)


fig2 = plt.figure(figsize=(15,20))

plt.subplot(4, 1, 1); plt.plot(axis_x_1[Signal_1], axis_y_1[Signal_1], "r"); plt.xlabel("Frequency(Hz)"); plt.title("Banda alfa");
plt.ylabel("Amplitud");
#Time Windows for Welchs method -  Alpha band
sr=1000
win = 4 * sr # 4 seconds time windows.

#FFT with time windows using scipy.signal.welch
axis_x_1, axis_y_1 = welch(senal_filtrada_eeg, sr, nperseg=win)


freq_low = 12 #lower limit for alpha band
freq_high = 30 #Upper limit for alpha band

Signal_1 = np.logical_and(axis_x_1 >= freq_low, axis_x_1 <= freq_high)


fig2 = plt.figure(figsize=(15,20))

plt.subplot(4, 1, 1); plt.plot(axis_x_1[Signal_1], axis_y_1[Signal_1], "r"); plt.xlabel("Frequency(Hz)"); plt.title("Banda beta");
plt.ylabel("Amplitud");

max_value = max(senal_filtrada_eeg)
min_value = min(senal_filtrada_eeg)
amplitude = max_value - min_value
mean = np.mean(senal_filtrada_eeg)
median_val = np.median(senal_filtrada_eeg)
std_val = np.std(senal_filtrada_eeg)
variance = np.var(senal_filtrada_eeg)

print(f'El valor máximo de la señal es: {max_value}')
print(f'El valor mínimo de la señal es: {min_value}')
print(f'La amplitud de la señal es: {amplitude}')
print(f'La media de la señal es: {mean}')
print(f'El valor medio de la señal es: {median_val}')
print(f'La desviación estandar de la señal es: {std_val}')
print(f'La varianza de la señal es: {variance}')