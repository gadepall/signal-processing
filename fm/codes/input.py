from scipy.fftpack import fft,fftshift
import numpy as np
from scipy.io import wavfile
import scipy.signal as signal
import matplotlib.pyplot as plt


#Fs, audio_data = wavfile.read("Sound.wav")
sample_rate, audio_data = wavfile.read("Sound.wav")

#perform fft on audio signal
i = np.fft.fft(audio_data)

#calculate the frequency range
f_i = np.fft.fftfreq(len(audio_data), d=1/sample_rate)

plt.plot(f_i, np.abs(i))
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude')
plt.title('Input Signal')
#plt.savefig('inputs.pdf')
plt.show()
# Calculate power spectral density
psd = np.abs(i)**2

# Calculate frequency range
freqs = np.fft.fftfreq(len(psd), 1/sample_rate)

# Find frequency range with significant power
mask = psd > 0.1*np.max(psd)
freq_range = freqs[mask]
bandwidth = max(freq_range) - min(freq_range)

print('Bandwidth:', bandwidth,'Hz')

