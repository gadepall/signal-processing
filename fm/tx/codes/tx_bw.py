'''==========================================================
Code by G V V Sharma
May 27, 2023,
Released under GNU/GPL
https://www.gnu.org/licenses/gpl-3.0.en.html
=========================================================='''
 
#Bandwidth of transmiited signal
 
from scipy.fftpack import fft
import numpy as np
from scipy.io import wavfile
import matplotlib.pyplot as plt

sample_rate, audio_data = wavfile.read("fm/input-audio/Sound.wav")


N = len(audio_data)
dt = 1e-3/N         # time span 1 msec
t = np.arange(N)
t1 = t*dt
fc = 100e6          #carrier frequency
kf = 20             # freq sensitivity

 
audio = 127*(audio_data.astype(np.int16)/ np.power(2,15))      #to convert audio file from signed 16-bit integer format to 8-bit unsigned integer
cumsum = np.cumsum(audio)                                 #Discrete summation

fm = np.cos(2*np.pi*fc*t1 + kf*cumsum*(1/sample_rate))    #equaion of fm signal

fm_fft = np.fft.fft(fm)
fm_psd = np.abs(fm_fft)**2
fm_freqs = np.fft.fftfreq(len(fm_psd), 1/sample_rate)

# Find frequency range with significant power of FM signal
threshold = 0.1*np.max(fm_psd)
fm_mask = fm_psd > threshold
fm_freq_range = fm_freqs[fm_mask]
fmax = max(fm_freq_range)
fmin = min(fm_freq_range)

fm_bandwidth = fmax - fmin
print('Bandwidth of tx signal:', fm_bandwidth, 'Hz')
