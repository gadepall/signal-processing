#Calculating Bandwith of the message signal

from scipy.fftpack import fft,fftshift
import numpy as np
from scipy.io import wavfile
import scipy.signal as signal
import matplotlib.pyplot as plt


#Fs, audio_data = wavfile.read("Sound.wav")
#Reading the audio data into the variable audio_data
sample_rate, audio_data = wavfile.read("fm/codes/msg/Sound_Noise.wav")

#perform fft on audio signal
X_i = np.fft.fft(audio_data)

# Calculate power spectral density
psd = np.abs(X_i)**2

# Calculate frequency range
freqs = np.fft.fftfreq(len(psd), 1/sample_rate)

# Find frequency range with significant power
mask = psd > 0.1*np.max(psd)
freq_range = freqs[mask]
bandwidth = max(freq_range) - min(freq_range)
print("fmax",max(freq_range))
print('fmin',min(freq_range))
print('Bandwidth:', bandwidth,'Hz')

