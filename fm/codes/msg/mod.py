from scipy.fftpack import fft,fftshift
import matplotlib.pyplot as plt
import numpy as np
from scipy.io import wavfile

# Load WAV file
sample_rate, audio = wavfile.read('Sound.wav')

# Perform FFT on signal
fft = np.fft.fft(audio)

# Calculate power spectral density
psd = np.abs(fft)**2

# Calculate frequency range
freqs = np.fft.fftfreq(len(psd), 1/sample_rate)

# Plotting input spectrum using power vs freq
plt.plot(freqs,psd)
plt.xlabel('Frequency (Hz)')
plt.ylabel('Power')
plt.title('Input Signal')
plt.show()

# Find frequency range with significant power
mask = psd > 0.1*np.max(psd)
freq_range = freqs[mask]
bandwidth = max(freq_range) - min(freq_range)

print('Bandwidth:', bandwidth,'Hz')

# Frequency modulation
fc = 100e6  # carrier frequency

N = len(audio)
dt = 1e-3/N             # time span 1 msec
t = np.arange(N)
t = t*dt

audio = 127*(audio.astype(np.int16)/ np.power(2,15))
ym = audio#[:,1] # Audio data



kf = 20              # freq sensitivity
cumsum = np.cumsum(ym)  # Discrete summation

c = np.cos(2*np.pi*fc*t)
y_fm = np.cos(2*np.pi*fc*t + kf*cumsum*(1/sample_rate))

fm_fft = np.fft.fft(y_fm)
f_1 = np.fft.fftfreq(len(y_fm), d=dt)

plt.plot(f_1,abs(fm_fft))
plt.xlabel('Frequency (Hz)')
plt.ylabel('Gain')
plt.grid(True)
plt.title('FM Signal')
plt.legend(loc='best')
plt.show()

# Calculate power spectral density of FM signal
fm_psd = np.abs(fm_fft)**2
# Calculate frequency range of FM signal
fm_freqs = np.fft.fftfreq(len(fm_psd), 1/sample_rate)

# Find frequency range with significant power of FM signal
fm_mask = fm_psd > 0.1*np.max(fm_psd)
fm_freq_range = fm_freqs[fm_mask]
fm_bandwidth = max(fm_freq_range) - min(fm_freq_range)
print('FM Bandwidth:', fm_bandwidth, 'Hz')
