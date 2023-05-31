
'''==========================================================
Code by G V V Sharma
May 27, 2023,
Released under GNU/GPL
https://www.gnu.org/licenses/gpl-3.0.en.html
=========================================================='''
 
#Spectrum of message signal using own FFT algorithm.
 
import numpy as np
from scipy.io import wavfile
import matplotlib.pyplot as plt

def fft(x):
    N = len(x)
    if N == 1:
        return x
    else:
        X_even = fft(x[::2])
        X_odd = fft(x[1::2])
        factor = np.exp(-2j * np.pi * np.arange(N) / N)
        return np.concatenate([X_even + factor[:N//2] * X_odd,
                               X_even + factor[N//2:] * X_odd])

sample_rate, audio_data = wavfile.read("fm/input-audio/Sound.wav")

# Zero padding
N = len(audio_data)
nextpow2 = int(np.ceil(np.log2(N)))
audio_data = np.pad(audio_data, (0, 2**nextpow2-N), mode='constant')

i = fft(audio_data)
f_i = np.fft.fftfreq(len(audio_data), d=1/sample_rate)

plt.plot(f_i, np.abs(i))
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude')
plt.title('Message Signal')
plt.savefig("fm/msg/figs/FFTalgorithm.pdf")
plt.show()

