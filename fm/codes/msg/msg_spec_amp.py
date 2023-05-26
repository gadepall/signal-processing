from scipy.fftpack import fft,fftshift
import numpy as np
from scipy.io import wavfile
import scipy.signal as signal
import matplotlib.pyplot as plt


#Fs, audio_data = wavfile.read("Sound.wav")
#Reading the audio data into the variable audio_data
sample_rate, audio_data = wavfile.read("fm/codes/msg/Sound_Noise.wav")
print(sample_rate)
#perform fft on audio signal
X_i = np.fft.fft(audio_data)

#calculate the frequency range
f_i = np.fft.fftfreq(len(audio_data), d=1/sample_rate)
print(f_i)

plt.plot(f_i, np.abs(X_i))
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude')
plt.title('Input Signal')
#plt.savefig('inputs.pdf')
plt.show()


