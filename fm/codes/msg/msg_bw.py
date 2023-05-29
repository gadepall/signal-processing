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

sample_rate, audio_data = wavfile.read("fm/codes/msg/Sound_Noise.wav")

X_i = np.fft.fft(audio_data)
psd = np.abs(X_i)**2
freqs = np.fft.fftfreq(len(psd), 1/sample_rate)

# Find frequency range with significant power
mask = psd > 0.1*np.max(psd)
freq_range = freqs[mask]
bandwidth = max(freq_range) - min(freq_range)
#print("fmax",max(freq_range))
#print('fmin',min(freq_range))
print('Bandwidth of msg signal:', bandwidth,'Hz')

