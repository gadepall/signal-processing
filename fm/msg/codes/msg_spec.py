'''==========================================================
Code by G V V Sharma
May 27, 2023,
Released under GNU/GPL
https://www.gnu.org/licenses/gpl-3.0.en.html
=========================================================='''
 
#Spectrum of message signal using builtin FFT algorithm of the python library ’Numpy'
 
from scipy.fftpack import fft
import numpy as np
from scipy.io import wavfile
import matplotlib.pyplot as plt

sample_rate, audio_data = wavfile.read("fm/input-audio/Sound.wav")
X_i = np.fft.fft(audio_data)
f_i = np.fft.fftfreq(len(audio_data), d=1/sample_rate)

plt.plot(f_i, np.abs(X_i))
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude')
plt.title('Message Signal')
plt.savefig("fm/msg/figs/msg_spec.pdf")
plt.show()

