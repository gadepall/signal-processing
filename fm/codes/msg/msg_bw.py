'''==========================================================
Code by G V V Sharma
May 27, 2023,
Released under GNU/GPL
https://www.gnu.org/licenses/gpl-3.0.en.html
=========================================================='''
 
#Calculating Bandwith of the message signal

from scipy.fftpack import fft
import numpy as np
from scipy.io import wavfile
import matplotlib.pyplot as plt

sample_rate, audio_data = wavfile.read("fm/input-audio/Sound.wav")

X_i = np.fft.fft(audio_data)
psd = np.abs(X_i)**2
freqs = np.fft.fftfreq(len(psd), 1/sample_rate)

# Find frequency range with significant power
threshold = 0.1*np.max(psd)
mask = psd > threshold

freq_range = freqs[mask]
fmax = max(freq_range)
fmin = min(freq_range)
print("f_max is:",fmax)
print("f_min is:",fmin)
bandwidth = fmax - fmin
print('Bandwidth of msg signal:', bandwidth,'Hz')

