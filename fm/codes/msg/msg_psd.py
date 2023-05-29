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

sample_rate, audio_data = wavfile.read("fm/codes/msg/Sound_Noise.wav")

X_i = np.fft.fft(audio_data)
psd = np.abs(X_i)**2
freqs = np.fft.fftfreq(len(psd), 1/sample_rate)

plt.plot(freqs,psd)
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude')
plt.title('psd of the message signal')
plt.savefig("fm/msg/figs/msg_psd.pdf")
plt.show()


