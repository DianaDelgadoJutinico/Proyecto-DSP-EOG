# -*- coding: utf-8 -*-
"""PROYECTO.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1CTlOa_gsEGJcV-MR1cHjvUam63zmOiXj
"""

!pip install mne
!pip install pymatreader

from google.colab import drive
drive.mount('/content/drive')

"""Paciente P15 visita 1/día 3/Sesión 7."""

import mne
import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq

# Ruta a los archivos de BrainVision
P15V01_path = '/content/drive/MyDrive/DSP proyecto/p15/v01 d03/p15_v01_d03_b07_spelller04.ahdr'

# Cargar los datos usando MNE
P15V01 = mne.io.read_raw_brainvision(P15V01_path, preload=True)
#raw = mne.io.read_raw_eeglab(eeg_path, preload=True)

# Mostrar información básica del conjunto de datos
print(P15V01.info)


# Graficar todos los canales EOG.

#EOG Right UP
P15V01_EORU = P15V01.get_data(picks='EOGRU')[0]  #obtener datos del canal EOGRU
sampling_rate = int(P15V01.info['sfreq'])  #Frecuencia de muestreo
#normalizar la señal
P15V01_EORU = (P15V01_EORU - np.mean(P15V01_EORU)) / np.std(P15V01_EORU)

#EOG Right Down
P15V01_EORD = P15V01.get_data(picks='EOGRD')[0]  #obtener datos del canal EOGRD
sampling_rate = int(P15V01.info['sfreq'])  #Frecuencia de muestreo

P15V01_EORD = (P15V01_EORD - np.mean(P15V01_EORD)) / np.std(P15V01_EORD)

#EOG Right Horizontal
P15V01_EORH = P15V01.get_data(picks='EOGRH')[0]  #obtener datos del canal EOGRH
sampling_rate = int(P15V01.info['sfreq'])  #Frecuencia de muestreo

P15V01_EORH = (P15V01_EORH - np.mean(P15V01_EORH)) / np.std(P15V01_EORH)

#EOG Left Horizontal
P15V01_EOLH = P15V01.get_data(picks='EOGLH')[0]  #obtener datos del canal EOGLH
sampling_rate = int(P15V01.info['sfreq'])  #Frecuencia de muestreo

P15V01_EOLH = (P15V01_EOLH - np.mean(P15V01_EOLH)) / np.std(P15V01_EOLH)

#Graficar canal EOG RIGHT UP.
plt.subplot(2, 1, 1)
plt.plot(P15V01_EORU)
plt.title('Señal EOG RU P15')
plt.xlabel('Tiempo (segundos)')
plt.ylabel('Amplitud (mV)')
plt.show()

#Graficar canal EOG RIGHT DOWN.
plt.subplot(2, 1, 2)
plt.plot(P15V01_EORD)
plt.title('Señal EOG RD P15')
plt.xlabel('Tiempo (segundos)')
plt.ylabel('Amplitud (mV)')
plt.show()

#Graficar canal EOG LEFT UP.
plt.subplot(2, 1, 1)
plt.plot(P15V01_EORH)
plt.title('Señal EOG RH P15')
plt.xlabel('Tiempo (segundos)')
plt.ylabel('Amplitud (mV)')
plt.show()

#Graficar canal EOG LEFT DOWN.
plt.subplot(2, 1, 2)
plt.plot(P15V01_EOLH)
plt.title('Señal EOG LH P15')
plt.xlabel('Tiempo (segundos)')
plt.ylabel('Amplitud (mV)')
plt.show()

"""Paciente P15 visita 1/día 3/Sesión 7. FFT"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft


# Calcular la FFT EOGRU
N = len(P15V01_EORU)               # Número de muestras
frequencies = np.fft.fftfreq(N, d=1/sampling_rate)  # Frecuencias correspondientes
fft_values = fft(P15V01_EORU)      # FFT de la señal

# Tomar la parte positiva del espectro (frecuencias >= 0)
positive_freqs_P15V01_EORU = frequencies[:N // 2]                  # Mitad positiva de las frecuencias
positive_fft_values_P15V01_EORU = np.abs(fft_values[:N // 2])      # Magnitud de la FFT

# Graficar el espectro de frecuencias positivo
plt.figure(figsize=(10, 6))
plt.plot(positive_freqs_P15V01_EORU, positive_fft_values_P15V01_EORU)
plt.title('Espectro de frecuencias de la señal EOG Right UP')
plt.xlabel('Frecuencia (Hz)')
plt.ylabel('Magnitud de la FFT')
plt.grid()
plt.xlim(0, sampling_rate / 2)  # Limitar el eje x a la mitad de la frecuencia de muestreo
plt.ylim(0,20000)
plt.show()


# Calcular la FFT EOGRD
N = len(P15V01_EORD)               # Número de muestras
frequencies = np.fft.fftfreq(N, d=1/sampling_rate)  # Frecuencias correspondientes
fft_values = fft(P15V01_EORD)      # FFT de la señal

# Tomar la parte positiva del espectro (frecuencias >= 0)
positive_freqs_P15V01_EORD = frequencies[:N // 2]                  # Mitad positiva de las frecuencias
positive_fft_values_P15V01_EORD = np.abs(fft_values[:N // 2])      # Magnitud de la FFT

# Graficar el espectro de frecuencias positivo
plt.figure(figsize=(10, 6))
plt.plot(positive_freqs_P15V01_EORD, positive_fft_values_P15V01_EORD)
plt.title('Espectro de frecuencias de la señal EOG Right DOWN')
plt.xlabel('Frecuencia (Hz)')
plt.ylabel('Magnitud de la FFT')
plt.grid()
plt.xlim(0, sampling_rate / 2)  # Limitar el eje x a la mitad de la frecuencia de muestreo
plt.ylim(0,20000)
plt.show()


# Calcular la FFT EOGRH
N = len(P15V01_EORH)               # Número de muestras
frequencies = np.fft.fftfreq(N, d=1/sampling_rate)  # Frecuencias correspondientes
fft_values = fft(P15V01_EORH)      # FFT de la señal

# Tomar la parte positiva del espectro (frecuencias >= 0)
positive_freqs_P15V01_EORH = frequencies[:N // 2]                  # Mitad positiva de las frecuencias
positive_fft_values_P15V01_EORH = np.abs(fft_values[:N // 2])      # Magnitud de la FFT

# Graficar el espectro de frecuencias positivo
plt.figure(figsize=(10, 6))
plt.plot(positive_freqs_P15V01_EORH, positive_fft_values_P15V01_EORH)
plt.title('Espectro de frecuencias de la señal EOG Right HORIZONTAL')
plt.xlabel('Frecuencia (Hz)')
plt.ylabel('Magnitud de la FFT')
plt.grid()
plt.xlim(0, sampling_rate / 2)  # Limitar el eje x a la mitad de la frecuencia de muestreo
plt.ylim(0,20000)
plt.show()


# Calcular la FFT EOGLH
N = len(P15V01_EOLH)               # Número de muestras
frequencies = np.fft.fftfreq(N, d=1/sampling_rate)  # Frecuencias correspondientes
fft_values = fft(P15V01_EOLH)      # FFT de la señal

# Tomar la parte positiva del espectro (frecuencias >= 0)
positive_freqs_P15V01_EOLH = frequencies[:N // 2]                  # Mitad positiva de las frecuencias
positive_fft_values_P15V01_EOLH = np.abs(fft_values[:N // 2])      # Magnitud de la FFT

# Graficar el espectro de frecuencias positivo
plt.figure(figsize=(10, 6))
plt.plot(positive_freqs_P15V01_EOLH, positive_fft_values_P15V01_EOLH)
plt.title('Espectro de frecuencias de la señal EOG Left HORIZONTAL')
plt.xlabel('Frecuencia (Hz)')
plt.ylabel('Magnitud de la FFT')
plt.grid()
plt.xlim(0, sampling_rate / 2)  # Limitar el eje x a la mitad de la frecuencia de muestreo
plt.ylim(0,20000)
plt.show()

"""Paciente P15 visita 1/día 3/Sesión 7. Filtro FIR"""

import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

# Especificaciones del filtro FIR Equirriple (remez)
fs = 500  # Frecuencia de muestreo
fpass = [10, 50]  # Frecuencias de paso
fstop = [7, 53]  # Frecuencias de rechazo
gpass = 1  # Rizado de banda pasante
gstop = 60  # Atenuación de banda rechazada

# Orden del filtro (ajustar según necesidades)
order = 50
numtaps = order + 1

# Diseño del filtro FIR Equirriple usando remez
b = signal.remez(numtaps, [0, fstop[0], fpass[0], fpass[1], fstop[1], 0.5 * fs], [0, 1, 0], fs=fs)

# Respuesta en frecuencia del filtro
w, h = signal.freqz(b)

# Gráfica de magnitud
plt.figure(figsize=(10, 5))
plt.subplot(2, 1, 1)
plt.plot(w / (2 * np.pi) * fs, 20 * np.log10(abs(h)))
plt.title('Respuesta en Magnitud del Filtro FIR Equirriple (remez)')
plt.xlabel('Frecuencia (Hz)')
plt.ylabel('Magnitud (dB)')
plt.grid(True)

# Líneas de referencia
plt.axvline(fpass[0], color='r', linestyle='--', label='fpass')
plt.axvline(fpass[1], color='r', linestyle='--', label='fpass')
plt.axvline(fstop[0], color='g', linestyle='--', label='fstop')
plt.axvline(fstop[1], color='g', linestyle='--', label='fstop')

plt.legend()
plt.ylim([-150, 10])

# Gráfica de fase
plt.subplot(2, 1, 2)
plt.plot(w / (2 * np.pi) * fs, np.unwrap(np.angle(h)))
plt.title('Respuesta en Fase del Filtro FIR Equirriple (remez)')
plt.xlabel('Frecuencia (Hz)')
plt.ylabel('Fase (radianes)')
plt.grid(True)

# Líneas de referencia
plt.axvline(fpass[0], color='r', linestyle='--', label='fpass')
plt.axvline(fpass[1], color='r', linestyle='--', label='fpass')
plt.axvline(fstop[0], color='g', linestyle='--', label='fstop')
plt.axvline(fstop[1], color='g', linestyle='--', label='fstop')

plt.tight_layout()
plt.show()

import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# Especificaciones del filtro FIR Equirriple (remez)
fs = 500  # Frecuencia de muestreo
fpass = [20, 50]  # Frecuencias de paso
fstop = [18, 53]  # Frecuencias de rechazo
gpass = 1  # Rizado de banda pasante
gstop = 20  # Atenuación de banda rechazada

# Orden del filtro (ajustar según necesidades)
order = 20
numtaps = order + 1

# Diseño del filtro FIR Equirriple usando remez
b = signal.remez(numtaps, [0, fstop[0], fpass[0], fpass[1], fstop[1], 0.5 * fs], [0, 1, 0], fs=fs)

# Extraer la señal del canal especificado
canal = 'EOGRU'  # Cambia esto al nombre del canal deseado
P15V01_data, times = P15V01.get_data(picks=canal), np.arange(0, len(P15V01.get_data(picks=canal)[0]) / P15V01.info['sfreq'], 1/P15V01.info['sfreq'])  # Extraer datos y tiempos correspondientes

# Aplicar el filtro a la señal usando filtfilt
filtered_signal = signal.filtfilt(b, 1, P15V01_data[0])  # `a=1` para filtro FIR

# Graficar señal original y filtrada
plt.figure(figsize=(12, 6))

# Señal original
plt.subplot(2, 1, 1)
plt.plot(times, P15V01_data[0], label='Señal Original')
plt.title(f'Señal Original del Canal {canal}')
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud (mV)')
plt.grid(True)
plt.legend()

# Señal filtrada
plt.subplot(2, 1, 2)
plt.plot(times, filtered_signal, label='Señal Filtrada', color='red')
plt.title(f'Señal Filtrada del Canal {canal}')
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud (mV)')
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()

import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# Especificaciones
fs = 500  # Frecuencia de muestreo
N = len(P15V01_data[0])  # Número de muestras de la señal

# Componente DC para la señal original
comp_DC_original = np.mean(P15V01_data[0])

# FFT de la señal original
fft_original = np.fft.fft(P15V01_data[0] - comp_DC_original, axis=0)
frequencies = np.fft.fftfreq(N, d=1/fs)
fft_original_magnitude = 2 * np.abs(fft_original[:N // 2]) / N

# Componente DC para la señal filtrada
comp_DC_filtered = np.mean(filtered_signal)

# FFT de la señal filtrada
fft_filtered = np.fft.fft(filtered_signal - comp_DC_filtered, axis=0)
fft_filtered_magnitude = 2 * np.abs(fft_filtered[:N // 2]) / N

# Graficar espectros de magnitud
plt.figure(figsize=(12, 6))
plt.plot(frequencies[:N // 2], fft_original_magnitude, label='Espectro Original', color='blue')
plt.plot(frequencies[:N // 2], fft_filtered_magnitude, label='Espectro Filtrado', color='red')
plt.title("Comparación de Espectros de Magnitud FFT (Filtro FIR Equirriple)")
plt.xlabel("Frecuencia (Hz)")
plt.ylabel("Magnitud")
plt.xlim([0, fs / 2])
plt.ylim([0, max(fft_original_magnitude.max(), fft_filtered_magnitude.max()) * 1.1])
plt.legend()
plt.grid(True)
plt.show()

"""Paciente P11 visita 7/día 2/Sesión 6."""

import mne
import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq

# Ruta a los archivos de BrainVision
P11V07_path = '/content/drive/MyDrive/DSP proyecto/p11/d02/p11_v07_d02_b07_speller06.vhdr'
# Cargar los datos usando MNE
P11V07 = mne.io.read_raw_brainvision(P11V07_path, preload=True)
#raw = mne.io.read_raw_eeglab(eeg_path, preload=True)

# Mostrar información básica del conjunto de datos
print(P11V07.info)

# Graficar todos los canales EOG.


#EOG Right UP
P11V07_EOGU = P11V07.get_data(picks='EOGU')[0]  #obtener datos del canal EOGU
sampling_rate = int(P11V07.info['sfreq'])  #Frecuencia de muestreo
#normalizar la señal
P11V07_EOGU = (P11V07_EOGU - np.mean(P11V07_EOGU)) / np.std(P11V07_EOGU)


#EOG Right Down
P11V07_EOGD = P11V07.get_data(picks='EOGD')[0]  #obtener datos del canal EOGD
sampling_rate = int(P11V07.info['sfreq'])  #Frecuencia de muestreo


P11V07_EOGD = (P11V07_EOGD - np.mean(P11V07_EOGD)) / np.std(P11V07_EOGD)


#EOG Right Horizontal
P11V07_EOGR = P11V07.get_data(picks='EOGR')[0]  #obtener datos del canal EOGR
sampling_rate = int(P11V07.info['sfreq'])  #Frecuencia de muestreo


P11V07_EOGR = (P11V07_EOGR - np.mean(P11V07_EOGR)) / np.std(P11V07_EOGR)


#EOG Left Horizontal
P11V07_EOGL = P11V07.get_data(picks='EOGL')[0]  #obtener datos del canal EOGL
sampling_rate = int(P11V07.info['sfreq'])  #Frecuencia de muestreo


P11V07_EOGL = (P11V07_EOGL - np.mean(P11V07_EOGL)) / np.std(P11V07_EOGL)


#Graficar canal EOG RIGHT UP.
plt.subplot(2, 1, 1)
plt.plot(P11V07_EOGU)
plt.title('Señal EOG RU P11')
plt.xlabel('Tiempo (segundos)')
plt.ylabel('Amplitud (mV)')
plt.show()


#Graficar canal EOG RIGHT DOWN.
plt.subplot(2, 1, 2)
plt.plot(P11V07_EOGD)
plt.title('Señal EOG RD P11')
plt.xlabel('Tiempo (segundos)')
plt.ylabel('Amplitud (mV)')
plt.show()


#Graficar canal EOG LEFT UP.
plt.subplot(2, 1, 1)
plt.plot(P11V07_EOGR)
plt.title('Señal EOG RH P11')
plt.xlabel('Tiempo (segundos)')
plt.ylabel('Amplitud (mV)')
plt.show()


#Graficar canal EOG LEFT DOWN.
plt.subplot(2, 1, 2)
plt.plot(P11V07_EOGL)
plt.title('Señal EOG LH P11')
plt.xlabel('Tiempo (segundos)')
plt.ylabel('Amplitud (mV)')
plt.show()

"""P11 V07 FFT"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft




# Calcular la FFT EOGRU
N = len(P11V07_EOGU)               # Número de muestras
frequencies = np.fft.fftfreq(N, d=1/sampling_rate)  # Frecuencias correspondientes
fft_values = fft(P11V07_EOGU)      # FFT de la señal


# Tomar la parte positiva del espectro (frecuencias >= 0)
positive_freqs_P11V07_EOGU = frequencies[:N // 2]                  # Mitad positiva de las frecuencias
positive_fft_values_P11V07_EOGU = np.abs(fft_values[:N // 2])      # Magnitud de la FFT


# Graficar el espectro de frecuencias positivo
plt.figure(figsize=(10, 6))
plt.plot(positive_freqs_P11V07_EOGU, positive_fft_values_P11V07_EOGU)
plt.title('Espectro de frecuencias de la señal EOG Right UP')
plt.xlabel('Frecuencia (Hz)')
plt.ylabel('Magnitud de la FFT')
plt.grid()
plt.xlim(0, sampling_rate / 2)  # Limitar el eje x a la mitad de la frecuencia de muestreo
plt.ylim(0,20000)
plt.show()




# Calcular la FFT EOGRD
N = len(P11V07_EOGD)               # Número de muestras
frequencies = np.fft.fftfreq(N, d=1/sampling_rate)  # Frecuencias correspondientes
fft_values = fft(P11V07_EOGD)      # FFT de la señal


# Tomar la parte positiva del espectro (frecuencias >= 0)
positive_freqs_P11V07_EOGD = frequencies[:N // 2]                  # Mitad positiva de las frecuencias
positive_fft_values_P11V07_EOGD = np.abs(fft_values[:N // 2])      # Magnitud de la FFT


# Graficar el espectro de frecuencias positivo
plt.figure(figsize=(10, 6))
plt.plot(positive_freqs_P11V07_EOGD, positive_fft_values_P11V07_EOGD)
plt.title('Espectro de frecuencias de la señal EOG Right DOWN')
plt.xlabel('Frecuencia (Hz)')
plt.ylabel('Magnitud de la FFT')
plt.grid()
plt.xlim(0, sampling_rate / 2)  # Limitar el eje x a la mitad de la frecuencia de muestreo
plt.ylim(0,20000)
plt.show()




# Calcular la FFT EOGRH
N = len(P11V07_EOGR)               # Número de muestras
frequencies = np.fft.fftfreq(N, d=1/sampling_rate)  # Frecuencias correspondientes
fft_values = fft(P11V07_EOGR)      # FFT de la señal


# Tomar la parte positiva del espectro (frecuencias >= 0)
positive_freqs_P11V07_EOGR = frequencies[:N // 2]                  # Mitad positiva de las frecuencias
positive_fft_values_P11V07_EOGR = np.abs(fft_values[:N // 2])      # Magnitud de la FFT


# Graficar el espectro de frecuencias positivo
plt.figure(figsize=(10, 6))
plt.plot(positive_freqs_P11V07_EOGR, positive_fft_values_P11V07_EOGR)
plt.title('Espectro de frecuencias de la señal EOG Right HORIZONTAL')
plt.xlabel('Frecuencia (Hz)')
plt.ylabel('Magnitud de la FFT')
plt.grid()
plt.xlim(0, sampling_rate / 2)  # Limitar el eje x a la mitad de la frecuencia de muestreo
plt.ylim(0,20000)
plt.show()




# Calcular la FFT EOGLH
N = len(P11V07_EOGL)               # Número de muestras
frequencies = np.fft.fftfreq(N, d=1/sampling_rate)  # Frecuencias correspondientes
fft_values = fft(P11V07_EOGL)      # FFT de la señal


# Tomar la parte positiva del espectro (frecuencias >= 0)
positive_freqs_P11V07_EOGL = frequencies[:N // 2]                  # Mitad positiva de las frecuencias
positive_fft_values_P11V07_EOGL = np.abs(fft_values[:N // 2])      # Magnitud de la FFT


# Graficar el espectro de frecuencias positivo
plt.figure(figsize=(10, 6))
plt.plot(positive_freqs_P11V07_EOGL, positive_fft_values_P11V07_EOGL)
plt.title('Espectro de frecuencias de la señal EOG Left HORIZONTAL')
plt.xlabel('Frecuencia (Hz)')
plt.ylabel('Magnitud de la FFT')
plt.grid()
plt.xlim(0, sampling_rate / 2)  # Limitar el eje x a la mitad de la frecuencia de muestreo
plt.ylim(0,20000)
plt.show()

import numpy as np
import matplotlib.pyplot as plt
from scipy import signal


# Especificaciones del filtro FIR Equirriple (remez)
fs = 500  # Frecuencia de muestreo
fpass = [20, 50]  # Frecuencias de paso
fstop = [18, 53]  # Frecuencias de rechazo
gpass = 1  # Rizado de banda pasante
gstop = 20  # Atenuación de banda rechazada


# Orden del filtro (ajustar según necesidades)
order = 20
numtaps = order + 1


# Diseño del filtro FIR Equirriple usando remez
b = signal.remez(numtaps, [0, fstop[0], fpass[0], fpass[1], fstop[1], 0.5 * fs], [0, 1, 0], fs=fs)


# Extraer la señal del canal especificado
canal = 'EOGU'  # Cambia esto al nombre del canal deseado
P11V07_data, times = P11V07.get_data(picks=canal), np.arange(0, len(P11V07.get_data(picks=canal)[0]) / P11V07.info['sfreq'], 1/P11V07.info['sfreq'])  # Extraer datos y tiempos correspondientes


# Aplicar el filtro a la señal usando filtfilt
filtered_signal = signal.filtfilt(b, 1, P11V07_data[0])  # `a=1` para filtro FIR


# Graficar señal original y filtrada
plt.figure(figsize=(12, 6))


# Señal original
plt.subplot(2, 1, 1)
plt.plot(times, P11V07_data[0], label='Señal Original')
plt.title(f'Señal Original del Canal {canal}')
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud (mV)')
plt.grid(True)
plt.legend()


# Señal filtrada
plt.subplot(2, 1, 2)
plt.plot(times, filtered_signal, label='Señal Filtrada', color='red')
plt.title(f'Señal Filtrada del Canal {canal}')
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud (mV)')
plt.grid(True)
plt.legend()


plt.tight_layout()
plt.show()

import numpy as np
import matplotlib.pyplot as plt
from scipy import signal


# Especificaciones
fs = 500  # Frecuencia de muestreo
N = len(P11V07_data[0])  # Número de muestras de la señal


# Componente DC para la señal original
comp_DC_original = np.mean(P11V07_data[0])


# FFT de la señal original
fft_original = np.fft.fft(P11V07_data[0] - comp_DC_original, axis=0)
frequencies = np.fft.fftfreq(N, d=1/fs)
fft_original_magnitude = 2 * np.abs(fft_original[:N // 2]) / N


# Componente DC para la señal filtrada
comp_DC_filtered = np.mean(filtered_signal)


# FFT de la señal filtrada
fft_filtered = np.fft.fft(filtered_signal - comp_DC_filtered, axis=0)
fft_filtered_magnitude = 2 * np.abs(fft_filtered[:N // 2]) / N


# Graficar espectros de magnitud
plt.figure(figsize=(12, 6))
plt.plot(frequencies[:N // 2], fft_original_magnitude, label='Espectro Original', color='blue')
plt.plot(frequencies[:N // 2], fft_filtered_magnitude, label='Espectro Filtrado', color='red')
plt.title("Comparación de Espectros de Magnitud FFT (Filtro FIR Equirriple)")
plt.xlabel("Frecuencia (Hz)")
plt.ylabel("Magnitud")
plt.xlim([0, fs / 2])
plt.ylim([0, max(fft_original_magnitude.max(), fft_filtered_magnitude.max()) * 1.1])
plt.legend()
plt.grid(True)
plt.show()