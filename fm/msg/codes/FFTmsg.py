import numpy as np
from scipy.io import wavfile
import scipy.signal as signal
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

# Load audio data
sample_rate, audio_data = wavfile.read("Sound.wav")

# Zero padding
N = len(audio_data)
nextpow2 = int(np.ceil(np.log2(N)))
audio_data = np.pad(audio_data, (0, 2**nextpow2-N), mode='constant')

# Perform FFT on audio signal
i = fft(audio_data)

# Calculate the frequency range
f_i = np.fft.fftfreq(len(audio_data), d=1/sample_rate)

# Plot the spectrum
plt.plot(f_i, np.abs(i))
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude')
plt.show()

