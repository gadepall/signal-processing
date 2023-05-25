#Plotting PSD of the message signal

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

#Plotting psd of msg signal
plt.plot(freqs,psd)
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude')
plt.title('psd of the message signal')
plt.savefig("fm/msg/figs/psd.pdf")
plt.show()


