'''==========================================================
Code by G V V Sharma
May 27, 2023,
Released under GNU/GPL
https://www.gnu.org/licenses/gpl-3.0.en.html
=========================================================='''
 
#Plotting power spectral density of the message signal

from scipy.fftpack import fft
import numpy as np
from scipy.io import wavfile
import matplotlib.pyplot as plt

sample_rate, audio_data = wavfile.read("fm/input-audio/Sound.wav")

X_i = np.fft.fft(audio_data)
psd = np.abs(X_i)**2
freqs = np.fft.fftfreq(len(psd), 1/sample_rate)


threshold = 0.1*np.max(psd)
mask = psd > threshold
freq_range = freqs[mask]
fmax = max(freq_range)
fmin = min(freq_range)
bandwidth = fmax - fmin


plt.plot(freqs,psd)
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude')
plt.title('psd of the message signal')
plt.axhline(y=threshold,color='red', ls='--')      #threshold limit
plt.vlines(ymin=0, ymax=threshold, x=[fmin,fmax], color='red', ls='--')   #range of frequencies which gives bandwidth of msg signal
plt.savefig("fm/msg/figs/msg_psd.pdf")
plt.show()

